# fora
# class AdminUsersView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminUsersView(AdminView):
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
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                self.template = 'fora:templates/admin/users/view.pt'
            elif self.activity == 'create':
                self.template = 'fora:templates/admin/users/create.pt'
            elif self.activity == 'edit':
                self.template = 'fora:templates/admin/users/edit.pt'
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminUsersView, self).prepare_template()
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
                'email_address': users[id].email_address()
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
