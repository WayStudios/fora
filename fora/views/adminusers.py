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
    identity = None
    def __init__(self, request):
        template = '%(path)s/users.pt' % {'path': AdminView.path['templates']}
        super(AdminUsersView, self).__init__(request = request,
                                             template = template,
                                             actions = {
                                                 'retrieve_users': self.retrieve_users,
                                                 'retrieve_user': self.retrieve_user,
                                                 'create_user': self.create_user,
                                                 'edit_user': self.edit_user,
                                                 'delete_user': self.delete_user
                                             })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                user = User.get_user_by_uuid(self.identity)
                self.value['user'] = {
                    'uuid': user.uuid(),
                    'username': user.username(),
                    'email_address': user.email_address(),
                    'is_active': user.is_active(),
                    'is_deleted': user.is_deleted(),
                    'create_date': user.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': user.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/users/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/users/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                user = User.get_user_by_uuid(self.identity)
                self.value['user'] = {
                    'uuid': user.uuid(),
                    'username': user.username(),
                    'email_address': user.email_address(),
                    'is_active': user.is_active(),
                    'is_deleted': user.is_deleted(),
                    'create_date': user.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': user.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/users/edit.pt' % {'path': AdminView.path['templates']}
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
            if not users[id].is_deleted():
                value['entries'].append({
                    'identity': users[id].uuid(),
                    'id': users[id].id(),
                    'username': users[id].username(),
                    'email_address': users[id].email_address(),
                    'is_active': users[id].is_active()
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
    def create_user(self):
        value = {
            'status': False,
            'error': 0
        }
        user = User.get_user_by_username(self.json['username'])
        if user.exists():
            value['error'] = 1
        if value['error'] == 0:
            user = User.get_user_by_email_address(self.json['email_address'])
            if user.exists():
                value['error'] = 2;
        if value['error'] == 0:
            User.create_user(username = self.json['username'], email_address = self.json['email_address'], password = self.json['password'])
            value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def edit_user(self):
        value = {
            'status': False,
            'error': 0
        }
        user = User.get_user_by_username(self.json['username'])
        if user.exists():
            if user.uuid() != self.json['uuid']:
                value['error'] = 1
        if value['error'] == 0:
            user = User.get_user_by_email_address(self.json['email_address'])
            if user.exists():
                if user.uuid() != self.json['uuid']:
                    value['error'] = 2
        if value['error'] == 0:
            user = User.get_user_by_uuid(self.json['uuid'])
            user.username(self.json['username'])
            user.email_address(self.json['email_address'])
            if 'password' in self.json:
                if self.json['password'] != '':
                    user.password(self.json['password'])
            value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_user(self):
        value = {
            'status': False
        }
        user = User.get_user_by_uuid(self.json['identity'])
        if user.exists():
            user.is_deleted(True)
            value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
