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
    def create_user(email, username, password):
        result = UserModel(uuid = str(uuid.uuid4()), email = email, username = username, password = password, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(result)
        obj = User()
        obj.model = result
        return obj
