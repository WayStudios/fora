# fora
# class ThreadModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class ThreadModel(Model):
    __tablename__ = 'threads'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    parent = Column(String)
    author = Column(String)
    subject = Column(String)
    content = Column(String)
    is_anonymous = Column(Boolean)
    is_archived = Column(Boolean)
    is_deleted = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
