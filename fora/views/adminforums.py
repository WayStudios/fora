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
        template = '%(path)s/forums.pt' % {'path': AdminView.path['templates']}
        super(AdminForumsView, self).__init__(request = request,
                                              template = template,
                                              actions = {
                                                  'retrieve_forums': self.retrieve_forums,
                                                  'retrieve_forum': self.retrieve_forum,
                                                  'create_forum': self.create_forum,
                                                  'edit_forum': self.edit_forum,
                                                  'delete_forum': self.delete_forum
                                              })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                forum = Forum.get_forum_by_uuid(self.identity)
                self.value['forum'] = {
                    'uuid': forum.uuid(),
                    'parent': forum.parent(),
                    'title': forum.title(),
                    'description': forum.description(),
                    'is_active': forum.is_active(),
                    'is_deleted': forum.is_deleted(),
                    'create_date': forum.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': forum.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                if self.value['forum']['parent'] == '':
                    self.value['forum']['parent'] = 'None'
                else:
                    forum = Forum.get_forum_by_uuid(self.value['forum']['parent'])
                    self.value['forum']['parent'] = forum.title()
                self.template = '%(path)s/forums/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.value['forums'] = {}
                forums = Forum.get_forums()
                for id in forums:
                    self.value['forums'][id] = {
                        'uuid': forums[id].uuid(),
                        'title': forums[id].title()
                    }
                self.template = '%(path)s/forums/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                forum = Forum.get_forum_by_uuid(self.identity)
                self.value['forum'] = {
                    'uuid': forum.uuid(),
                    'parent': forum.parent(),
                    'title': forum.title(),
                    'description': forum.description(),
                    'is_active': forum.is_active(),
                    'is_deleted': forum.is_deleted(),
                    'create_date': forum.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': forum.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.value['forums'] = {}
                forums = Forum.get_forums()
                for id in forums:
                    if id != forum.id() and forums[id].parent() != forum.uuid():
                        self.value['forums'][id] = {
                            'uuid': forums[id].uuid(),
                            'title': forums[id].title()
                        }
                self.template = '%(path)s/forums/edit.pt' % {'path': AdminView.path['templates']}
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
            parent = forums[id].parent()
            if parent == '':
                parent = 'None'
            else:
                forum = Forum.get_forum_by_uuid(parent)
                parent = forum.title()
            value['entries'].append({
                'identity': forums[id].uuid(),
                'id': forums[id].id(),
                'title': forums[id].title(),
                'parent': parent,
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
    def create_forum(self):
        value = {
            'status': False,
            'error': 0
        }
        Forum.create_forum(title = self.json['title'], description = self.json['description'], parent = self.json['parent'], is_active = self.json['is_active'])
        value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def edit_forum(self):
        value = {
            'status': False,
            'error': 0
        }
        forum = Forum.get_forum_by_uuid(self.json['uuid'])
        forum.parent(self.json['parent'])
        forum.title(self.json['title'])
        forum.description(self.json['description'])
        forum.is_active(self.json['is_active'])
        value['status'] = True
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_forum(self):
        value = {
            'status': True,
            'error': 0
        }
        forum = Forum.get_forum_by_uuid(self.json['identity'])
        if forum:
            forum.is_deleted(True)
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
