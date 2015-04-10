# fora
# class Configuration
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import DBSession

from fora.models.configuration import ConfigurationModel

class Configuration(object):
    """ This class contains core functionality of fora configuration manipulation.
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
    def type(self, new_type = None):
        if not new_type:
            return self.model.type
        self.model.type = new_type
    def name(self, new_name = None):
        if not new_name:
            return self.model.name
        self.model.name = new_name
    def value(self, new_value = None):
        if not new_value:
            return self.model.value
        self.model.value = new_value
    def create_date(self, new_create_date = None):
        if not new_create_date:
            return self.model.create_date
        self.model.create_date = new_create_date
    def update_date(self, new_update_date = None):
        if not new_update_date:
            return self.model.update_date
        self.model.update_date = new_update_date
    @staticmethod
    def get_configuration_by_name(name):
        result = DBSession.query(ConfigurationModel).filter(ConfigurationModel.name == name).first()
        if result:
            obj = Configuration()
            obj.model = result
            return obj
        return None
