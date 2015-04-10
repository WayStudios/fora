# fora
# class AdminTopicsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminTopicsView(View):
    """ This class contains the topics administration view of fora.
    """
    def __init__(self, request):
        super(AdminTopicsView, self).__init__(request = request,
                                              template = None,
                                              actions = {
                                              })
