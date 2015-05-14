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
        template = '%(path)s/articles.pt' % {'path': AdminView.path['templates']}
        super(AdminArticlesView, self).__init__(request = request,
                                                template = template,
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
                    'description': article.description(),
                    'content': article.content(),
                    'is_active': article.is_active(),
                    'create_date': article.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': article.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/articles/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/articles/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                article = Article.get_article_by_uuid(self.identity)
                self.value['article'] = {
                    'uuid': article.uuid(),
                    'title': article.title(),
                    'content': article.content(),
                    'description': article.description(),
                    'is_active': article.is_active(),
                    'create_date': article.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': article.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/articles/edit.pt' % {'path': AdminView.path['templates']}
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
                'is_active': articles[id].is_active(),
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
