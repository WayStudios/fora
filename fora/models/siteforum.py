# fora
# class SiteForumModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String
)

class SiteForumModel(Model):
    __tablename__ = 'sites_forums'
    id = Column(Integer, primary_key = True, autoincrement = True)
    site = Column(String)
    forum = Column(String)
