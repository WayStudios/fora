# fora
# class AdminDashboardView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminDashboardView(AdminView):
    """ This class contains the administration dashboard view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/dashboard.pt' % {'path': AdminView.path['templates']}
        super(AdminDashboardView, self).__init__(request = request,
                                                 template = template,
                                                 actions = {
                                                 })
    def prepare_template(self):
        if self.moderator.is_guest():
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminDashboardView, self).prepare_template()
