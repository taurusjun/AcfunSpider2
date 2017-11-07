#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义数据库模型实体
Desc : 
"""
import datetime

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from settings import DATABASE


def create_news_table(engine):
    """"""
    Base.metadata.create_all(engine)


def _get_date():
    return datetime.datetime.now()

Base = declarative_base()

class ACComment(Base):
    """文章类"""
    __tablename__ = 'accomment'

    cid = Column(BigInteger, primary_key=True)
    acid = Column(BigInteger)
    quoteId = Column(BigInteger)
    content = Column(Text)
    postDate = Column(DateTime)
    userID = Column(BigInteger)
    userName = Column(String(120))
    userImg = Column(String(300))
    localImgPath = Column(String(300))
    count = Column(Integer)
    deep = Column(Integer)
    refCount = Column(Integer)
    ups = Column(Integer)
    downs = Column(Integer)
    nameRed = Column(Integer)
    avatarFrame = Column(Integer)
    isDelete = Column(Boolean)
    isUpDelete = Column(Boolean)
    nameType = Column(Integer)
    verified = Column(Integer)
    verifiedText = Column(Text)
    updateDate = Column(DateTime)

class ACCommentCache(Base):
    """文章类"""
    __tablename__ = 'accommentcache'

    cid = Column(BigInteger, primary_key=True)
    acid = Column(BigInteger)
    quoteId = Column(BigInteger)
    content = Column(Text)
    postDate = Column(DateTime)
    userID = Column(BigInteger)
    userName = Column(String(120))
    userImg = Column(String(300))
    localImgPath = Column(String(300))
    count = Column(Integer)
    deep = Column(Integer)
    refCount = Column(Integer)
    ups = Column(Integer)
    downs = Column(Integer)
    nameRed = Column(Integer)
    avatarFrame = Column(Integer)
    isDelete = Column(Boolean)
    isUpDelete = Column(Boolean)
    nameType = Column(Integer)
    verified = Column(Integer)
    verifiedText = Column(Text)
