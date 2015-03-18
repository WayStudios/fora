# fora
# class UserView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

from pyramid.renderers import render_to_response

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
        self.value['identity'] = request.matchdict['identity']
    def login_user(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def logout_user(self):
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
