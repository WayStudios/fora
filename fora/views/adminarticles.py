# fora
# class AdminArticlesView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.article import Article

from pyramid.renderers import render_to_response

class AdminArticlesView(View):
    """ This class contains the articles administration view of fora.
    """
    def __init__(self, request):
        super(AdminArticlesView, self).__init__(request = request,
                                                template = 'fora:templates/admin/articles.pt',
                                                actions = {
                                                    'retrieve_articles': self.retrieve_articles,
                                                    'retrieve_article': self.retrieve_article,
                                                    'delete_article': self.delete_article
                                                })
    def retrieve_articles(self):
        value = {
            'status': True,
            'entries': []
        }
        articles = Article.get_articles()
        for id in articles:
            value['entries'].append({
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
