# fora
# class ForumModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

class ForumModel(Model):
    __tablename__ = 'forums'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    title = Column(String)
    description = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
