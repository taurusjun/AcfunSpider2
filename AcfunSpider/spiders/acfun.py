#!/usr/bin/python
#coding=utf8

import scrapy
import re
import json

import time

from pydispatch import dispatcher
from scrapy import signals, exceptions
from scrapy.spiders import CrawlSpider

from AcfunSpider.DBOperation import DBOperation
from AcfunSpider.items import *
from lru import LRU


class AcfunSpider(CrawlSpider):
    name = "acfun"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "http://www.acfun.cn/v/list110/index.htm"
        # "http://www.acfun.cn/a/ac3998668"
    ]
    _cache = LRU(10240)

    def __init__(self):
        self.logger.info("initlizing...")
        self.DBUtils=DBOperation()
        self.DBUtils.loadACfunCommentItemsToCache(self._cache)
        self.DBUtils.clearCacheItemInDB()
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
            yield scrapy.Request(url=x, callback=self.parse0, dont_filter=True)

    def parse0(self, response):
        # body_data = response.body;
        # parse_data = self.get_parse_data(body_data);
        # self.log('Hi, we get response!')
        replyListItems = self.parse_reply_list(response)
        for itm in replyListItems:
            acid = itm['link'][0][5:]
            url = "http://www.acfun.cn/comment_list_json.aspx?contentId=" + str(acid) + "&currentPage=1"
            yield scrapy.Request(url, meta={'acid':str(acid)}, callback=self.parse_comment_contents, dont_filter=True)

        # print 1
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

    # 主内容区：xpath: '//div[@id="mainer"]//div[@id="block-content-article"]//div[@class="mainer"]/div[@class="item"]/a/@href'
    # 最新回复区：xpath: //div[@id="mainer"]//div[@id="block-reply-article"]//div[@class="mainer"]//a/@href'
    def parse_reply_list(self, response):
        for sel in response.xpath('//div[@id="mainer"]//div[@id="block-reply-article"]//div[@class="mainer"]//a'):
            item = AcfunItem()
            item['title'] = sel.xpath('@title').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item

    # 解析评论
    def parse_comment_contents(self,response):
        acid = response.meta['acid']
        jsonresponse = json.loads(response.body_as_unicode())
        responseStatus = jsonresponse[u'status']
        responseSuccess = jsonresponse[u'success']
        if responseStatus == 200 and responseSuccess == True:
            commentsList = jsonresponse[u'data'][u'commentContentArr']
            # 开始解析json评论
            for m, n in enumerate(commentsList):
                commentJson = commentsList[n]
                commentItem = AcfunCommentItem(commentJson)
                # 设定acid
                commentItem['acid'] = acid
                # 默认是float，转成long
                commentItem['cid'] = long(commentItem['cid'])
                commentItem['quoteId'] = long(commentItem['quoteId'])
                commentItem['userID'] = long(commentItem['userID'])
                yield commentItem

    def spider_idle(self):
        self.logger.info("Now LRU size is %s" % len(self._cache))
        self.logger.info("Sleep 3s and try next query...")
        time.sleep(3)
        self.logger.info("---------------Next round query---------------")
        for url in self.start_urls:
            self.crawler.engine.crawl(self.create_request(url), self)
        raise scrapy.exceptions.DontCloseSpider("I want to live a little longer...")

    def create_request(self,url):
        return scrapy.Request(url=url, callback=self.parse0, dont_filter=True)

    def close(spider, reason):
        spider.DBUtils.saveMemeItems(spider._cache)
        spider.logger.info("close it with reason: %s!" % str(reason))