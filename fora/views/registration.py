# fora
# class RegistrationView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class RegistrationView(View):
    """ This class contains the registration view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/registration.pt' % {'path': View.path['templates']}
        super(RegistrationView, self).__init__(request = request,
                                               template = template,
                                               actions = {
                                                   'create_user': self.create_user
                                               })
        self.title = self.localizer.translate('Registration', domain = 'fora')
    def create_user(self):
        email_address = self.json['email_address']
        username = self.json['username']
        password = self.json['password']
        User.create_user(email_address = email_address, username = username, password = password)
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def prepare_template(self):
        if not self.user.is_guest():
            self.exception = HTTPFound(self.request.route_url("portal"))
        super(RegistrationView, self).prepare_template()
