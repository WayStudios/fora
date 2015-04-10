# fora
# class Site
# Xu [xw901103@gmail.com] Copyright 2015

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
    def create_date(self, new_create_date = None):
        if not new_create_date:
            return self.model.create_date
        self.model.create_date = new_create_date
    def update_date(self, new_update_date = None):
        if not new_update_date:
            return self.model.update_date
        self.model.update_date = new_update_date
