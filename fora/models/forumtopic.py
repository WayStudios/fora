# fora
# class ForumTopicModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String
)

class ForumTopicModel(Model):
    __tablename__ = 'forums_topics'
    id = Column(Integer, primary_key = True, autoincrement = True)
    forum_uuid = Column(String)
    topic_uuid = Column(String)
