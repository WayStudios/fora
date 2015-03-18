# fora
# class AdminView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminView(View):
    """ This class contains the administration view of fora.
    """
    def __init__(self, request):
        super(AdminView, self).__init__(request = request,
                                        template = 'fora:templates/admin.pt',
                                        actions = {
                                        })
