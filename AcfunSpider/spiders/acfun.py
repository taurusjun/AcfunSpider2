#!/usr/bin/python
#coding=utf8

import scrapy
import re
import json
import time

from pydispatch import dispatcher
from scrapy import signals, exceptions
from scrapy.spiders import CrawlSpider

from AcfunSpider.IPProxy import IPProxy
from AcfunSpider.utils import utils
from AcfunSpider.items import *
from lru import LRU
from datetime import datetime

from AcfunSpider import settings
if settings.TEST_MODE:
    from AcfunSpider.DBDummyOperation import DBDummyOperation as DBOperation 
else:
    from AcfunSpider.DBOperation import DBOperation as DBOperation 

class AcfunSpider(CrawlSpider):
    name = "acfun"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.acfun.cn/v/list110/index.htm"
        "http://webapi.aixifan.com/query/article/list?pageNo=1&size=10&realmIds=5,1,2,4&originalOnly=false&orderType=1&filterTitleImage=true"
    ]
    _cache = LRU(20480)

    def __init__(self, *args, **kwargs):
        self.logger.info("initlizing...")
        super(AcfunSpider, self).__init__(*args, **kwargs)
        self.DBUtils=DBOperation()
        self.DBUtils.loadACfunCommentItemsToCache(self._cache)
        self.DBUtils.clearCacheItemInDB()
        self.IPProxy = IPProxy()
        # dispatcher.connect(self.spider_idle, signals.spider_idle)
        self.logger.info("initlizing...Done.")

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        from_crawler = super(AcfunSpider, cls).from_crawler
        spider = from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_idle, signal=scrapy.signals.spider_idle)
        return spider

    # def __init__(self, *args, **kwargs):
    #     super(AcfunSpider, self).__init__(*args, **kwargs)
    #     dispatcher.connect(self.spider_idle, signals.spider_idle)

    def start_requests(self):
        for x in self.start_urls:
            proxy = self.IPProxy.getProxy('http')
            self.logger.info("http proxy:%s"%proxy)
            try:
                yield scrapy.Request(url=x, callback=self.parse0, meta={'proxy':proxy},dont_filter=True)
            except Exception as e:
                self.logger.error("proxy: %s not usable"%proxy )

    def parse0(self, response):
        replyListItems = self.parse_reply_list(response)
        for itm in replyListItems:
            acid = itm['acid']
            title = itm['title']
            # 20190825 更新评论获取接口
            # url = "http://www.acfun.cn/comment_list_json.aspx?contentId=" + str(acid) + "&currentPage=1"
            # 旧版评论
            url = "https://www.acfun.cn/rest/pc-direct/comment/listByFloor?sourceId=" + str(acid) + "&sourceType=3&page=1"
            # 新版评论
            # url = "https://www.acfun.cn/rest/pc-direct/comment/list?sourceId=" + str(acid) + "&sourceType=3&page=1"
            proxy = self.IPProxy.getProxy('https')
            self.logger.info("https proxy:%s"%proxy)
            yield scrapy.Request(url, meta={'acid':str(acid),'title':title,'proxy':proxy}, callback=self.parse_comment_contents, dont_filter=True)

        # print 1
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

    # 主内容区：xpath: '//div[@id="mainer"]//div[@id="block-content-article"]//div[@class="mainer"]/div[@class="item"]/a/@href'
    # 最新回复区：xpath: //div[@id="mainer"]//div[@id="block-reply-article"]//div[@class="mainer"]//a/@href'
    # 2017/12/08 Acfun终于改版了，完全改成SPA形式，这样就不用去解析页面元素了，噢耶
    def parse_reply_list(self, response):
        # 2017/12/08 下面的页面解析不用了
        # for sel in response.xpath('//div[@id="mainer"]//div[@id="block-reply-article"]//div[@class="mainer"]//a'):
        #     item = AcfunItem()
        #     item['title'] = sel.xpath('@title').extract()
        #     item['link'] = sel.xpath('@href').extract()
        #     yield item

        # 2017/12/08 开始完全采用SPA，纯ajax取得数据
        jsonresponse = json.loads(response.body_as_unicode())
        code = jsonresponse['code']
        if code == 200:
            articleList = jsonresponse[u'data'][u'articleList']
            for m, article in enumerate(articleList):
                item = AcfunItem()
                item['title'] = article[u'title']
                item['acid'] = article[u'id']
                yield item

    # 解析评论
    def parse_comment_contents(self,response):
        acid = response.meta['acid']
        title = response.meta['title']

        jsonresponse = json.loads(response.body_as_unicode())
        commentCount = jsonresponse.get(u'totalCount')
        if commentCount and commentCount > 0:
            commentsList = jsonresponse.get(u'commentsMap')
            # 开始解析json评论
            for m, n in enumerate(commentsList):
                commentJson = commentsList[n]
                try:
                    commentItem = AcfunCommentItem()
                    # 设定acid
                    commentItem['acid'] = acid
                    # 设定title
                    commentItem['title'] = title
                    # 默认是float，转成long
                    commentItem['cid'] = long(commentJson['cid'])
                    commentItem['quoteId'] = long(commentJson['quoteId'])
                    commentItem['content'] = commentJson['content']
                    #postDate处理，postDate必须是datetime类型
                    postDate = commentJson['postDate']
                    commentItem['postDate'] = utils.convetStrToDatetime(postDate)                    
                    commentItem['userID'] = long(commentJson['userId'])
                    commentItem['userName'] = commentJson['userName']
                    commentItem['userImg'] = commentJson['avatarImage']
                    # commentItem['count'] = commentJson['count']
                    commentItem['deep'] = commentJson['floor']
                    commentItem['isSignedUpCollege'] = commentJson['isSignedUpCollege']
                    # commentItem['refCount'] = commentJson['refCount']
                    # commentItem['ups'] = commentJson['ups']
                    # commentItem['downs'] = commentJson['downs']
                    commentItem['nameRed'] = commentJson['nameRed']
                    commentItem['avatarFrame'] = commentJson['avatarFrame']
                    commentItem['isDelete'] = commentJson['isDelete']
                    commentItem['isUpDelete'] = commentJson['isUpDelete']
                    # commentItem['nameType'] = commentJson['nameType']
                    commentItem['verified'] = commentJson['verified']
                    # commentItem['updateDate'] = commentJson['updateDate']
                    # commentItem['verifiedText'] = commentJson['verifiedText']
                    yield commentItem
                except Exception,e:
                    self.logger.error(str(e))
                    self.logger.error("Error!commentJson:%s" % str(commentJson))
                    pass

    def spider_idle(self):
        self.logger.info("Now LRU size is %s" % len(self._cache))
        self.logger.info("Sleep 3s and try next query...")
        time.sleep(3)
        self.logger.info("---------------Next round query---------------")
        for url in self.start_urls:
            self.crawler.engine.crawl(self.create_request(url), self)
        raise scrapy.exceptions.DontCloseSpider("I want to live a little longer...")

    def create_request(self,url):
        proxy = self.IPProxy.getProxy('http')
        self.logger.info("next round start -- http proxy:%s"%proxy)
        return scrapy.Request(url=url, callback=self.parse0, meta={'proxy':proxy}, dont_filter=True)

    def close(self,spider, reason):
        spider.DBUtils.saveMemeItems(spider._cache)
        spider.logger.info("close it with reason: %s!" % str(reason))