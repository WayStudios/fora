# fora
# class Page
# Xu [xw901103@gmail.com] Copyright 2015

class Page(object):
    """ This class contains core functionality of fora page manipulation.
    """
    model = None
    def __init__(self):
        self.model = None
    def title(self, new_title = None):
        if not new_title:
            return self.model.title
        self.model.title = new_title
    def description(self, new_description = None):
        if not new_description:
            return self.model.description
        self.model.description = new_description
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
    def get_page_by_uuid(uuid):
        result = DBSession.query(PageModel).filter(PageModel.uuid == uuid).first()
        obj = Page()
        obj.model = result
        return obj
