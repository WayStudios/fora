# fora
# class AdminArticlesView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminArticlesView(View):
    """ This class contains the articles administration view of fora.
    """
    def __init__(self, request):
        super(AdminArticlesView, self).__init__(request = request,
                                                template = None,
                                                actions = {
                                                })
