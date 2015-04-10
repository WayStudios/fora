# fora
# class AdminForumsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminForumsView(View):
    """ This class contains the forums administration view of fora.
    """
    def __init__(self, request):
        super(AdminForumsView, self).__init__(request = request,
                                              template = None,
                                              actions = {
                                              })
