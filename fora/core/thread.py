# fora
# class Thread
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import DBSession

from fora.models.thread import ThreadModel

import uuid
from datetime import datetime

class Thread(object):
    """ This class contains core functionality of fora thread manipulation.
    """
    model = None
    def __init__(self, model = None):
        self.model = model
    def id(self):
        return self.model.id
    def uuid(self, new_uuid = None):
        if not new_uuid:
            return self.model.uuid
        self.model.uuid = new_uuid
    def parent(self, new_parent = None):
        if not new_parent:
            return self.model.parent
        self.model.parent = new_parent
    def author(self, new_author = None):
        if not new_author:
            return self.model.author
        self.model.author = new_author
    def subject(self, new_subject = None):
        if not new_subject:
            return self.model.subject
        self.model.subject = new_subject
    def content(self, new_content = None):
        if not new_content:
            return self.model.content
        self.model.content = new_content
    def is_archived(self, new_is_archived = None):
        if not new_is_archived:
            return self.model.is_archived
        self.model.is_archived = new_is_archived
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
    def get_thread_by_uuid(uuid):
        result = DBSession.query(ThreadModel).filter(ThreadModel.uuid == uuid).first()
        if not result:
            return None
        obj = Thread()
        obj.model = result
        return obj
    @staticmethod
    def get_threads():
        results = DBSession.query(ThreadModel).all()
        objs = {}
        for result in results:
            objs[result.id] = Thread()
            objs[result.id].model = result
        return objs
    @staticmethod
    def create_thread(parent = None, author = '', subject = '', content = '', is_archived = False, is_deleted = False):
        thread_uuid = str(uuid.uuid4())
        create_date = datetime.utcnow()
        if not parent:
            parent = thread_uuid
        result = ThreadModel(uuid = thread_uuid, parent = parent, author = author, subject = subject, content = content, is_archived = is_archived, is_deleted = is_deleted, create_date = create_date, update_date = create_date)
        DBSession.add(result)
        thread = Thread()
        thread.model = result
        return thread
