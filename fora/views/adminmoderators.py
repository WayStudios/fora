# fora
# class AdminModeratorsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.moderator import Moderator

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminModeratorsView(AdminView):
    """ This class contains the moderators administration view of fora.
    """
    def __init__(self, request):
        super(AdminModeratorsView, self).__init__(request = request,
                                                  template = 'fora:templates/admin/moderators.pt',
                                                  actions = {
                                                      'retrieve_moderators': self.retrieve_moderators
                                                  })
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                self.template = 'fora:templates/admin/moderators/view.pt'
            elif self.activity == 'create':
                self.template = 'fora:templates/admin/moderators/create.pt'
            elif self.activity == 'edit':
                self.template = 'fora:templates/admin/moderators/edit.pt'
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminModeratorsView, self).prepare_template()
    def retrieve_moderators(self):
        value = {
            'status': True,
            'entries': []
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
