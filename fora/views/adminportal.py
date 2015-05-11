# fora
# class AdminPortalView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminPortalView(AdminView):
    """ This class contains the administration portal view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/portal.pt' % {'path': AdminView.path['templates']}
        super(AdminPortalView, self).__init__(request = request,
                                              template = template,
                                              actions = {
                                                  'login_moderator': self.login_moderator,
                                                  'logout_moderator': self.logout_moderator
                                              })
        self.title = 'Administration'
    def prepare_template(self):
        if not self.moderator.is_guest():
            self.exception = HTTPFound(self.request.route_url("admin_dashboard"))
        super(AdminPortalView, self).prepare_template()
    def login_moderator(self):
        value = {
            'status': False
        }
        moderator = User.get_user_by_identity(self.json['identity'])
        if not moderator.is_guest():
            if moderator.password() == self.json['password']:
                self.session['moderator'] = moderator.uuid()
                self.session.changed()
                value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def logout_moderator(self):
        self.session['moderator'] = None
        self.session.invalidate()
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
