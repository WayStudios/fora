# fora
# class AdminUsersView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.user import User

from pyramid.renderers import render_to_response

class AdminUsersView(View):
    """ This class contains the users administration view of fora.
    """
    def __init__(self, request):
        super(AdminUsersView, self).__init__(request = request,
                                             template = 'fora:templates/admin/users.pt',
                                             actions = {
                                                 'retrieve_users': self.retrieve_users,
                                                 'retrieve_user': self.retrieve_user,
                                                 'delete_user': self.delete_user
                                             })
    def retrieve_users(self):
        value = {
            'status': True,
            'entries': []
        }
        users = User.get_users()
        for id in users:
            value['entries'].append({
                'id': users[id].id(),
                'username': users[id].username(),
                'email': users[id].email()
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_user(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_user(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
