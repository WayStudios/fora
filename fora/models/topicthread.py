# fora
# class TopicThreadModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String
)

class TopicThreadModel(Model):
    __tablename__ = 'topics_threads'
    id = Column(Integer, primary_key = True, autoincrement = True)
    topic = Column(String)
    thread = Column(String)
