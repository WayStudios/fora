# fora
# class AdminForumsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.forum import Forum

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminForumsView(AdminView):
    """ This class contains the forums administration view of fora.
    """
    def __init__(self, request):
        super(AdminForumsView, self).__init__(request = request,
                                              template = 'fora:templates/admin/forums.pt',
                                              actions = {
                                                  'retrieve_forums': self.retrieve_forums,
                                                  'retrieve_forum': self.retrieve_forum,
                                                  'delete_forum': self.delete_forum
                                              })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                self.template = 'fora:templates/admin/forums/view.pt'
            elif self.activity == 'create':
                self.template = 'fora:templates/admin/forums/create.pt'
            elif self.activity == 'edit':
                self.template = 'fora:templates/admin/forums/edit.pt'
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminForumsView, self).prepare_template()
    def retrieve_forums(self):
        value = {
            'status': True,
            'entries': []
        }
        forums = Forum.get_forums()
        for id in forums:
            value['entries'].append({
                'id': forums[id].id(),
                'title': forums[id].title(),
                'is_active': forums[id].is_active(),
                'is_deleted': forums[id].is_deleted(),
                'create_date': forums[id].create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': forums[id].update_date().strftime('%Y-%m-%d %H:%M:%S')
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_forum(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_forum(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
