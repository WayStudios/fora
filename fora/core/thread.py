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
    def create_thread(parent = None, author = '', subject = '', content = ''):
        thread_uuid = str(uuid.uuid4())
        create_date = datetime.utcnow()
        if not parent:
            parent = thread_uuid
        result = ThreadModel(uuid = thread_uuid, parent = parent, author = author, subject = subject, content = content, create_date = create_date, update_date = create_date)
        DBSession.add(result)
        thread = Thread()
        thread.model = result
        return thread
