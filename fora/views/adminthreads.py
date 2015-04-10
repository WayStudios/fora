# fora
# class AdminThreadsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminThreadsView(View):
    """ This class contains the threads administration view of fora.
    """
    def __init__(self, request):
        super(AdminThreadsView, self).__init__(request = request,
                                               template = None,
                                               actions = {
                                               })
