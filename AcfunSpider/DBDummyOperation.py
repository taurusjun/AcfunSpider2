#!/usr/bin/python
#coding=utf8
# -*- coding: utf-8 -*-

import logging

DBOperationLogging = logging.getLogger("DBDummyOperation")

class DBDummyOperation:
    def __init__(self):
        DBOperationLogging.info("DB initilized!")

    def saveItem(self,item):
            DBOperationLogging.info("Save item success! item: %s" % str(item))

    def loadACfunCommentItemsToCache(self, cacheContainer):
        DBOperationLogging.info("0 items loaded from DB!")

    def clearCacheItemInDB(self):
        DBOperationLogging.info("0 cached items deleted!")

    def saveMemeItems(self, cacheContainer):
        DBOperationLogging.info("0 memory items saved!")
