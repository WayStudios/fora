# fora
# class Moderator
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import (
    DBSession,
    OR
)
from fora.core.user import User

from fora.models.moderator import ModeratorModel

import uuid
from datetime import datetime

class Moderator(object):
    """ This class contains core functionality of fora moderator manipulation.
    """
    model = None
    def __init__(self):
        self.model = None
    def exists(self):
        return self.model != None
    def id(self):
        return self.model.id
    def user(self, new_user = None):
        if not new_user:
            return self.model.user
        self.model.user = new_user
    def email_address(self, new_mail_address = None):
        user = User.get_user_by_identity(self.user())
        if not new_email_address:
            return user.email_address()
        user.email_address(new_mail_address)
    def username(self, new_username = None):
        user = User.get_user_by_identity(self.user())
        if not new_username:
            return user.username()
        user.username(new_username)
    def password(self, new_password):
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
    def get_moderator_by_uuid(uuid):
        result = DBSession.query(ModeratorModel).filter(ModeratorModel.uuid == uuid).first()
        obj = Moderator()
        obj.model = result
        return obj
    @staticmethod
    def get_moderator_by_email_address(email_address):
        user = User.get_user_by_email_address(email_address)
        return Moderator.get_moderator_by_uuid(user.uuid())
    @staticmethod
    def get_moderator_by_username(username):
        user = User.get_user_by_username(username)
        return Moderator.get_moderator_by_uuid(user.uuid())
    @staticmethod
    def get_moderator_by_identity(identity):
        user = User.get_user_by_identity(identity)
        return Moderator.get_moderator_by_uuid(user.uuid())
    @staticmethod
    def get_moderators():
        results = DBSession.query(ModeratorModel).all()
        objs = {}
        for result in results:
            objs[result.id] = Moderator()
            objs[result.id].model = result
        return objs
    @staticmethod
    def create_moderator(user, password, is_active = True, is_deleted = False):
        result = ModeratorModel(user = user, password = password, is_active = is_active, is_deleted = is_deleted, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(result)
        obj = Moderator()
        obj.model = result
        return obj
