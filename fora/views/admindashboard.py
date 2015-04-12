# fora
# class AdminDashboardView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

class AdminDashboardView(View):
    """ This class contains the administration dashboard view of fora.
    """
    def __init__(self, request):
        super(AdminDashboardView, self).__init__(request = request,
                                                 template = 'fora:templates/admin/dashboard.pt',
                                                 actions = {
                                                 })
