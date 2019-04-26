#!/usr/bin/python
#coding=utf8
# -*- coding: utf-8 -*-

import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from AcfunSpider.items import AcfunCommentItem
from AcfunSpider.models import create_news_table, ACCommentCache
from AcfunSpider.settings import DATABASE

DBOperationLogging = logging.getLogger("DBOperation")

@contextmanager
def session_scope(Session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

class DBOperation:
    def __init__(self):
        engine = create_engine(URL(**DATABASE))
        create_news_table(engine)
        self.DBSession = sessionmaker(bind=engine)
        DBOperationLogging.info("DB initilized!")

    def saveItem(self,item):
        try:
            with session_scope(self.DBSession) as ss:
                ss.add(item)
            DBOperationLogging.info("Save item success! item: %s" % str(item))
        except Exception,e:
            DBOperationLogging.error(e)
            DBOperationLogging.error("Save item failed! item: %s"% str(item))

    def loadACfunCommentItemsToCache(self, cacheContainer):
        session = self.DBSession()
        mysqlClause = "SELECT * FROM accommentcache where postDate > DATE_SUB(NOW(), INTERVAL 1 day)  order by postDate asc"
        accItems = session.execute(mysqlClause).fetchall()
        for accItm in accItems:
            itm = AcfunCommentItem()
            itm['cid']=accItm[0]
            itm['acid'] = accItm[1]
            itm['quoteId'] = accItm[2]
            itm['content'] = accItm[3]
            itm['postDate'] = accItm[4]
            itm['userID'] = accItm[5]
            itm['userName'] = accItm[6]
            itm['userImg'] = accItm[7]
            itm['localImgPath'] = accItm[8]
            itm['count'] = accItm[9]
            itm['deep'] = accItm[10]
            itm['refCount'] = accItm[11]
            itm['ups'] = accItm[12]
            itm['downs'] = accItm[13]
            itm['nameRed'] = accItm[14]
            itm['avatarFrame'] = accItm[15]
            itm['isDelete'] = accItm[16]
            itm['isUpDelete'] = accItm[17]
            itm['nameType'] = accItm[18]
            itm['verified'] = accItm[19]
            itm['verifiedText'] = accItm[20]
            cid = itm['cid']
            cacheContainer[cid] = itm
        itemCount = len(accItems)
        DBOperationLogging.info("%s items loaded from DB!" % itemCount)
        session.close()

    def clearCacheItemInDB(self):
        with session_scope(self.DBSession) as ss:
            try:
                num_rows_deleted = ss.query(ACCommentCache).delete()
                DBOperationLogging.info("%s cached items deleted!" % num_rows_deleted)
            except:
                DBOperationLogging.info("Clear cached items failed!")

    def saveMemeItems(self, cacheContainer):
        session = self.DBSession()
        itemCount = len(cacheContainer)
        for itm in cacheContainer.values():
            mDict = itm.copy()
            del mDict['title']
            accmt = ACCommentCache(**mDict)
            session.merge(accmt)
        session.commit()
        session.close()
        DBOperationLogging.info("%s memory items saved!" % itemCount)
