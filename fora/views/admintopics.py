# fora
# class AdminTopicsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.topic import Topic
from fora.core.thread import Thread

from pyramid.renderers import render_to_response

class AdminTopicsView(View):
    """ This class contains the topics administration view of fora.
    """
    def __init__(self, request):
        super(AdminTopicsView, self).__init__(request = request,
                                              template = 'fora:templates/admin/topics.pt',
                                              actions = {
                                                  'retrieve_topics': self.retrieve_topics,
                                                  'retrieve_topic': self.retrieve_topic,
                                                  'delete_topic': self.delete_topic
                                              })
    def retrieve_topics(self):
        value = {
            'status': True,
            'entries': []
        }
        topics = Topic.get_topics()
        for id in topics:
            thread = Thread.get_thread_by_uuid(uuid = topics[id].initial_thread())
            value['entries'].append({
                'id': topics[id].id(),
                'author': thread.author(),
                'subject': thread.subject(),
                'is_archived': topics[id].is_archived(),
                'is_deleted': topics[id].is_deleted(),
                'create_date': topics[id].create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': topics[id].update_date().strftime('%Y-%m-%d %H:%M:%S')
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_topic(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_topic(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
