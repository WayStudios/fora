# fora
# class AdminArticlesView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.article import Article

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminArticlesView(AdminView):
    """ This class contains the articles administration view of fora.
    """
    identity = None
    def __init__(self, request):
        super(AdminArticlesView, self).__init__(request = request,
                                                template = 'fora:templates/admin/articles.pt',
                                                actions = {
                                                    'retrieve_articles': self.retrieve_articles,
                                                    'retrieve_article': self.retrieve_article,
                                                    'delete_article': self.delete_article
                                                })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                article = Article.get_article_by_uuid(self.identity)
                self.value['article'] = {
                    'uuid': article.uuid(),
                    'title': article.title(),
                    'content': article.content(),
                    'create_date': article.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': article.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = 'fora:templates/admin/articles/view.pt'
            elif self.activity == 'create':
                self.template = 'fora:templates/admin/articles/create.pt'
            elif self.activity == 'edit':
                self.template = 'fora:templates/admin/articles/edit.pt'
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminArticlesView, self).prepare_template()
    def retrieve_articles(self):
        value = {
            'status': True,
            'entries': []
        }
        articles = Article.get_articles()
        for id in articles:
            value['entries'].append({
                'identity': articles[id].uuid(),
                'id': articles[id].id(),
                'title': articles[id].title(),
                'create_date': articles[id].create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': articles[id].update_date().strftime('%Y-%m-%d %H:%M:%S')
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_article(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_article(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
