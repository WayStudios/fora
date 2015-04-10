# fora
# class RegistrationView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.user import User

from pyramid.renderers import render_to_response

class RegistrationView(View):
    """ This class contains the registration view of fora.
    """
    def __init__(self, request):
        super(RegistrationView, self).__init__(request = request,
                                               template = 'fora:templates/registration.pt',
                                               actions = {
                                                   'create_user': self.create_user
                                               })
    def create_user(self):
        email = self.json['email']
        username = self.json['username']
        password = self.json['password']
        User.create_user(email = email, username = username, password = password)
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
