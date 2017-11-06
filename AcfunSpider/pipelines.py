# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from AcfunSpider.models import ACComment


class AcfunspiderPipeline(object):
    def process_item(self, item, spider):
        return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from contextlib import contextmanager
from datetime import datetime
from logging.handlers import RotatingFileHandler

# formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s')
# handler = RotatingFileHandler("Pipeline.log", maxBytes=3 * 1024 * 1024)
# handler.setFormatter(formatter)
# pipelineLogging.addHandler(handler)
pipelineLogging = logging.getLogger("Pipeline")

class CachePipeline(object):
    def open_spider(self, spider):
        self._lru = spider._cache
        pipelineLogging.info("CachePipeline opend")

    # def process_item(self, item, spider):
    #     cid = item['cid']
    #     lruItem = self._lru.get(cid, None)
    #     if not lruItem:
    #         pipelineLogging.info("Add new item!!")
    #         item['updateDate'] = datetime.now()
    #         accmt = ACComment(**item)
    #         self._DBOp.saveItem(accmt)
    #     self._lru[cid] = item
    #     pipelineLogging.info("Now Cache size is %s" % len(self._lru))

    def process_item(self, item, spider):
        cid = item['cid']
        isDelete = item['isDelete'] or item['isUpDelete'] or item['userID'] == -1
        lruItem = self._lru.get(cid, None)
        if(isDelete and lruItem):
            pipelineLogging.info("=========== CachePipeline Find deleted item= " + str(lruItem))
            lruItem['isDelete'] = item['isDelete']
            lruItem['isUpDelete'] = item['isUpDelete']
            del self._lru[cid]
            pipelineLogging.info("Delete item cid= %s in LRU, \n Now size is %s" % (cid, len(self._lru)))
            return lruItem
        else:
            if(not isDelete):
                self._lru[cid]=item
                if(not lruItem):
                    pipelineLogging.debug("Add item to LRU, now size is %s" % len(self._lru))
            # pipelineLogging.info("Duplicate item found: cid = %s" % cid)
            raise DropItem("Drop duplicate item:")

class DBPipeline(object):

    def open_spider(self, spider):
        self._DBOp = spider.DBUtils
        pipelineLogging.info("DBPipeline opend")

    # def close_spider(self, spider):
    #     pipelineLogging.info("DBPipeline closed")

    def process_item(self, item, spider):

        item['updateDate'] = datetime.now()
        accmt = ACComment(**item)
        self._DBOp.saveItem(accmt)
        pipelineLogging.info("Item saved: %s" % str(item))
        return item


class MyImagesPipeline(ImagesPipeline):
    """先安装：pip install Pillow"""

    def get_media_requests(self, item, info):
        image_url = item['userImg']
        return [scrapy.Request(image_url)]

    def item_completed(self, results, item, info):
        if(results[0][0]):
            item['localImgPath'] = results[0][1]['path']

        pipelineLogging.info("MyImagesPipeline item_completed item %s " % str(item['cid']))
        return item
