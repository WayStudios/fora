# fora
# class PageView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class PageView(View):
    """ This class contains the page view of fora.
    """
    def __init__(self, request):
        super(PageView, self).__init__(request = request,
                                       template = 'fora:templates/page.pt',
                                       actions = {
                                       })
        self.value['identity'] = request.matchdict['identity']
