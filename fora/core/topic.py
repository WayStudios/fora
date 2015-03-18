# fora
# class Topic
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import (
    DBSession,
    ASC,
    DESC
)
from fora.core.thread import Thread

from fora.models.topic import TopicModel
from fora.models.thread import ThreadModel
from fora.models.topicthread import TopicThreadModel

import uuid
from datetime import datetime

class Topic(object):
    """ This class contains core functionality of fora topic manipulation.
    """
    model = None
    def __init__(self):
        self.model = None
    def uuid(self, new_uuid = None):
        if not new_uuid:
            return self.model.uuid
        self.model.uuid = new_uuid
    def subject(self, new_subject = None):
        thread = Thread.get_thread_by_uuid(self.initial_thread())
        if not new_subject:
            return thread.subject()
        thread.subject(new_subject)
    def initial_thread(self, new_initial_thread = None):
        if not new_initial_thread:
            return self.model.initial_thread
        self.model.initial_thread = new_initial_thread
    def create_date(self, new_create_date = None):
        if not new_create_date:
            return self.model.create_date
        self.model.create_date = new_create_date
    def update_date(self, new_update_date = None):
        if not new_update_date:
            return self.model.update_date
        self.model.update_date = new_update_date
    def get_threads(self, order_asc = ThreadModel.id):
        results = DBSession.query(ThreadModel).filter(ThreadModel.uuid == TopicThreadModel.thread_uuid, TopicThreadModel.topic_uuid == self.model.uuid).order_by(ASC(order_asc)).all()
        objs = {}
        for result in results:
            objs[result.uuid] = Thread()
            objs[result.uuid].model = result
        return objs
    def create_thread(self, parent = None, author = '', subject = '', content = ''):
        thread = Thread.create_thread(parent = parent, author = author, subject = subject, content = content)
        result = TopicThreadModel(topic_uuid = self.model.uuid, thread_uuid = thread.model.uuid)
        DBSession.add(result)
        return thread
    @staticmethod
    def get_topic_by_uuid(uuid):
        result = DBSession.query(TopicModel).filter(TopicModel.uuid == uuid).first()
        obj = Topic()
        obj.model = result
        return obj
    @staticmethod
    def create_topic(author, subject, content):
        thread = Thread.create_thread(author = author, subject = subject, content = content)
        topic_uuid = str(uuid.uuid4())
        create_date = thread.model.create_date
        result = TopicModel(uuid = topic_uuid, initial_thread = thread.model.uuid, create_date = create_date, update_date = create_date)
        DBSession.add(result)
        topic = Topic()
        topic.model = result
        result = TopicThreadModel(topic_uuid = topic.model.uuid, thread_uuid = thread.model.uuid)
        DBSession.add(result)
        return topic
