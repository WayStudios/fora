# fora
# class ArticleModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class ArticleModel(Model):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    title = Column(String)
    description = Column(String)
    content = Column(String)
    is_active = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
