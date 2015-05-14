# fora
# class Site
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import (
    DBSession
)

from fora.models.site import SiteModel

class Site(object):
    """ This class contains core functionality of fora site manipulation.
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
    def is_active(self, new_is_active = None):
        if new_is_active == None:
            return self.model.is_active
        self.model.is_active = new_is_active
    def create_date(self, new_create_date = None):
        if not new_create_date:
            return self.model.create_date
        self.model.create_date = new_create_date
    def update_date(self, new_update_date = None):
        if not new_update_date:
            return self.model.update_date
        self.model.update_date = new_update_date
    @staticmethod
    def get_site_by_uuid(uuid):
        result = DBSession.query(SiteModel).filter(SiteModel.uuid == uuid).first()
        if result:
            obj = Site()
            obj.model = result
            return obj
        return None
    @staticmethod
    def get_sites():
        results = DBSession.query(SiteModel).all()
        objs = {}
        for result in results:
            objs[result.id] = Site()
            objs[result.id].model = result
        return objs
