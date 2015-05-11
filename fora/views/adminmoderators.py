# fora
# class AdminModeratorsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.moderator import Moderator
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminModeratorsView(AdminView):
    """ This class contains the moderators administration view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/moderators.pt' % {'path': AdminView.path['templates']}
        super(AdminModeratorsView, self).__init__(request = request,
                                                  template = template,
                                                  actions = {
                                                      'retrieve_moderators': self.retrieve_moderators
                                                  })
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                self.template = '%(path)s/moderators/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/moderators/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                self.template = '%(path)s/moderators/edit.pt' % {'path': AdminView.path['templates']}
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminModeratorsView, self).prepare_template()
    def retrieve_moderators(self):
        value = {
            'status': True,
            'entries': []
        }
        moderators = Moderator.get_moderators()
        for id in moderators:
            user = User.get_user_by_uuid(moderators[id].user())
            value['entries'].append({
                'identity': moderators[id].user(),
                'id': moderators[id].id(),
                'username': user.username(),
                'email_address': user.email_address()
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
