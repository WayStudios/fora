# fora
# class AdminThreadsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.thread import Thread
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminThreadsView(AdminView):
    """ This class contains the threads administration view of fora.
    """
    identity = None
    def __init__(self, request):
        template = '%(path)s/threads.pt' % {'path': AdminView.path['templates']}
        super(AdminThreadsView, self).__init__(request = request,
                                               template = template,
                                               actions = {
                                                   'retrieve_threads': self.retrieve_threads,
                                                   'retrieve_thread': self.retrieve_thread,
                                                   'delete_thread': self.delete_thread
                                               })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                thread = Thread.get_thread_by_uuid(self.identity)
                self.value['thread'] = {
                    'uuid': thread.uuid(),
                    'subject': thread.subject(),
                    'author': thread.author(),
                    'content': thread.content(),
                    'is_anonymous': thread.is_anonymous(),
                    'is_archived': thread.is_archived(),
                    'is_deleted': thread.is_deleted(),
                    'create_date': thread.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': thread.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                if not thread.is_anonymous():
                    user = User.get_user_by_identity(thread.author())
                    self.value['thread']['username'] = user.username()
                self.template = '%(path)s/threads/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/threads/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                self.template = '%(path)s/threads/edit.pt' % {'path': AdminView.path['templates']}
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminThreadsView, self).prepare_template()
    def retrieve_threads(self):
        value = {
            'status': True,
            'entries': []
        }
        threads = Thread.get_threads()
        for id in threads:
            value['entries'].append({
                'identity': threads[id].uuid(),
                'id': threads[id].id(),
                'author': threads[id].author(),
                'subject': threads[id].subject(),
                'is_anonymous': threads[id].is_anonymous(),
                'is_archived': threads[id].is_archived(),
                'is_deleted': threads[id].is_deleted(),
                'create_date': threads[id].create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': threads[id].update_date().strftime('%Y-%m-%d %H:%M:%S')
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_thread(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_thread(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
