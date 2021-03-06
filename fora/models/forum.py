# fora
# class ForumModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class ForumModel(Model):
    __tablename__ = 'forums'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    parent = Column(String)
    title = Column(String)
    description = Column(String)
    is_active = Column(Boolean)
    is_deleted = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
