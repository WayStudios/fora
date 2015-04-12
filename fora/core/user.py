# fora
# class User
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import DBSession
from fora.models.user import UserModel

import uuid
from datetime import datetime

class User(object):
    """ This class contains core functionality of fora user manipulation.
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
    def email(self, new_email = None):
        if not new_email:
            return self.model.email
        self.model.email = new_email
    def username(self, new_username = None):
        if not new_username:
            return self.model.username
        self.model.username = new_username
    def password(self, new_password = None):
        if not new_password:
            return self.model.password
        self.model.password = new_password
    def is_active(self, new_is_active):
        if not new_is_active:
            return self.model.is_active
        self.model.is_active = new_is_active
    def is_deleted(self, new_is_deleted):
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
    def get_user_by_email(email):
        result = DBSession.query(UserModel).filter(UserModel.email == email).first()
        obj = User()
        obj.model = result
        return obj
    @staticmethod
    def get_user_by_username(username):
        result = DBSession.query(UserModel).filter(UserModel.username == username).first()
        obj = User()
        obj.model = result
        return obj
    @staticmethod
    def get_users():
        results = DBSession.query(UserModel).all()
        objs = {}
        for result in results:
            objs[result.id] = User()
            objs[result.id].model = result
        return objs
    @staticmethod
    def create_user(email, username, password, is_active = True, is_deleted = False):
        result = UserModel(uuid = str(uuid.uuid4()), email = email, username = username, password = password, is_active = is_active, is_deleted = is_deleted, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(result)
        obj = User()
        obj.model = result
        return obj
