# fora
# class UserView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPForbidden
)

class UserView(View):
    """ This class contains the user view of fora.
    """
    def __init__(self, request):
        super(UserView, self).__init__(request = request,
                                       template = 'fora:templates/user.pt',
                                       actions = {
                                           'login_user': self.login_user,
                                           'logout_user': self.logout_user,
                                           'activate_user': self.activate_user
                                       })
        self.title = self.localizer.translate('User', 'fora')
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        user = User.get_user_by_identity(self.value['identity'])
        if user.is_guest():
            self.exception = HTTPNotFound()
        else:
            self.title = self.localizer.translate('User ${user_username}', domain = 'fora', mapping = {'user_username': user.username()})
            self.value['user'] = {
                'uuid': user.uuid(),
                'username': user.username(),
                'email': user.email()
            }
        super(UserView, self).prepare_template()
    def login_user(self):
        value = {
            'status': False
        }
        user = User.get_user_by_identity(self.json['identity'])
        if not user.is_guest():
            if user.password() == self.json['password']:
                self.session['user'] = user.uuid()
                self.session.changed()
                value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def logout_user(self):
        self.session['user'] = None
        self.session.invalidate()
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def activate_user(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
