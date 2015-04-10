# fora
# class AdminUsersView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminUsersView(View):
    """ This class contains the users administration view of fora.
    """
    def __init__(self, request):
        super(AdminUsersView, self).__init__(request = request,
                                             template = None,
                                             actions = {
                                             })
