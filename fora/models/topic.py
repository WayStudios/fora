# fora
# class TopicModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class TopicModel(Model):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    initial_thread = Column(String, unique = True)
    is_archived = Column(Boolean)
    is_deleted = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
