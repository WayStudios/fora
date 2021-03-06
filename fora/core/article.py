# fora
# class Article
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import DBSession

from fora.models.article import ArticleModel

class Article(object):
    """ This class contains core functionality of fora article manipulation.
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
    def content(self, new_content = None):
        if not new_content:
            return self.model.content
        self.model.content = new_content
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
    def get_article_by_uuid(uuid):
        result = DBSession.query(ArticleModel).filter(ArticleModel.uuid == uuid).first()
        if not result:
            return None
        obj = Article()
        obj.model = result
        return obj
    @staticmethod
    def get_articles():
        results = DBSession.query(ArticleModel).all()
        objs = {}
        for result in results:
            objs[result.id] = Article()
            objs[result.id].model = result
        return objs
    @staticmethod
    def create_article(title = '', description = '', content = '', is_active = True):
        result = ArticleModel(uuid = str(uuid.uuid4()), is_active = is_active, is_deleted = is_deleted, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(result)
        obj = Article()
        obj.model = result
        return obj
