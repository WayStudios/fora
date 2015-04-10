# fora
# class AdminPortalView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminPortalView(View):
    """ This class contains the administration portal view of fora.
    """
    def __init__(self, request):
        super(AdminPortalView, self).__init__(request = request,
                                              template = 'fora:templates/admin/portal.pt',
                                              actions = {
                                              })
        self.title = 'Administration'
