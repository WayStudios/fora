# fora
# class ArticleView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class ArticleView(View):
    """ This class contains the article view of fora.
    """
    def __init__(self, request):
        super(ArticleView, self).__init__(request = request,
                                          template = 'fora:templates/article.pt',
                                          actions = {
                                          })
        self.value['identity'] = request.matchdict['identity']
