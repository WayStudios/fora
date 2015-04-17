# fora
# class Forum
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import DBSession
from fora.core.topic import Topic

from fora.models.forum import ForumModel
from fora.models.topic import TopicModel
from fora.models.forumtopic import ForumTopicModel

import uuid
from datetime import datetime

class Forum(object):
    """ This class contains core functionality of fora forum manipulation.
    """
    model = None
    def __init__(self):
        self.model = None
    def id(self):
        return self.model.id
    def uuid(self, new_uuid = None):
        if not new_uuid:
            return self.model.uuid
        self.model.uuid = new_uuid
    def title(self, new_title = None):
        if not new_title:
            return self.model.title
        self.model.title = new_title
    def description(self, new_description = None):
        if not new_description:
            return self.model.description
        self.model.description = new_description
    def is_active(self, new_is_active = None):
        if not new_is_active:
            return self.model.is_active
        self.model.is_active = new_is_active
    def is_deleted(self, new_is_deleted = None):
        if not new_is_deleted:
            return self.model.is_deleted
        self.model.is_deleted = new_is_deleted
    def create_date(self, new_create_date = None):
        if not new_create_date:
            return self.model.create_date
        self.model.create_date = new_create_date
    def update_date(self, new_update_date = None):
        if not new_update_date:
            return self.model.update_date
        self.model.update_date = new_update_date
    @staticmethod
    def create_forum(title, description, is_active = True, is_deleted = False):
        result = ForumModel(uuid = str(uuid.uuid4()), title = title, description = description, is_active = is_active, is_deleted = is_deleted, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(result)
        obj = Forum()
        obj.model = result
        return obj
    def create_topic(self, author, subject, content, is_anonymous = False, is_archived = False, is_deleted = False):
        topic = Topic.create_topic(author = author, subject = subject, content = content, is_anonymous = is_anonymous, is_archived = is_archived, is_deleted = is_deleted)
        result = ForumTopicModel(forum_uuid = self.model.uuid, topic_uuid = topic.model.uuid)
        DBSession.add(result)
        return topic
    def get_topics(self):
        results = DBSession.query(TopicModel).filter(TopicModel.uuid == ForumTopicModel.topic_uuid, ForumTopicModel.forum_uuid == self.model.uuid).all()
        objs = {}
        for result in results:
            objs[result.id] = Topic()
            objs[result.id].model = result
        return objs
    @staticmethod
    def get_forum_by_uuid(uuid):
        result = DBSession.query(ForumModel).filter(ForumModel.uuid == uuid).first()
        if not result:
            return None
        obj = Forum()
        obj.model = result
        return obj
    @staticmethod
    def get_forums():
        results = DBSession.query(ForumModel).all()
        objs = {}
        for result in results:
            objs[result.id] = Forum()
            objs[result.id].model = result
        return objs
