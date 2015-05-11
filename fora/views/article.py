# fora
# class ArticleView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.article import Article

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPForbidden
)

class ArticleView(View):
    """ This class contains the article view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/article.pt' % {'path': View.path['templates']}
        super(ArticleView, self).__init__(request = request,
                                          template = template,
                                          actions = {
                                          })
        self.title = self.localizer.translate('Article', domain = 'fora')
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        article = Article.get_article_by_uuid(self.value['identity'])
        if not article:
            self.exception = HTTPNotFound()
        else:
            self.title = self.localizer.translate('Article ${article_title}', domain = 'fora', mapping = {'article_title': article.title()})
            self.value['article'] = {
                'title': article.title(),
                'description': article.description(),
                'content': article.content(),
                'create_date': article.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': article.update_date().strftime('%Y-%m-%d %H:%M:%S')
            }
        super(ArticleView, self).prepare_template()
