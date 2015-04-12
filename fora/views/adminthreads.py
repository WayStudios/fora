# fora
# class AdminThreadsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.thread import Thread

from pyramid.renderers import render_to_response

class AdminThreadsView(View):
    """ This class contains the threads administration view of fora.
    """
    def __init__(self, request):
        super(AdminThreadsView, self).__init__(request = request,
                                               template = 'fora:templates/admin/threads.pt',
                                               actions = {
                                                   'retrieve_threads': self.retrieve_threads,
                                                   'retrieve_thread': self.retrieve_thread,
                                                   'delete_thread': self.delete_thread
                                               })
    def retrieve_threads(self):
        value = {
            'status': True,
            'entries': []
        }
        threads = Thread.get_threads()
        for id in threads:
            value['entries'].append({
                'id': threads[id].id(),
                'author': threads[id].author(),
                'subject': threads[id].subject(),
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
