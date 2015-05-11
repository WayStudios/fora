# fora
# class AdminTopicsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.topic import Topic
from fora.core.thread import Thread

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminTopicsView(AdminView):
    """ This class contains the topics administration view of fora.
    """
    identity = None
    def __init__(self, request):
        template = '%(path)s/topics.pt' % {'path': AdminView.path['templates']}
        super(AdminTopicsView, self).__init__(request = request,
                                              template = template,
                                              actions = {
                                                  'retrieve_topics': self.retrieve_topics,
                                                  'retrieve_topic': self.retrieve_topic,
                                                  'delete_topic': self.delete_topic
                                              })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                topic = Topic.get_topic_by_uuid(self.identity)
                thread = Thread.get_thread_by_uuid(topic.initial_thread())
                self.value['topic'] = {
                    'uuid': topic.uuid(),
                    'subject': thread.subject(),
                    'content': thread.content(),
                    'create_date': topic.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': topic.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/topics/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/topics/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                self.template = '%(path)s/topics/edit.pt' % {'path': AdminView.path['templates']}
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminTopicsView, self).prepare_template()
    def retrieve_topics(self):
        value = {
            'status': True,
            'entries': []
        }
        topics = Topic.get_topics()
        for id in topics:
            thread = Thread.get_thread_by_uuid(uuid = topics[id].initial_thread())
            value['entries'].append({
                'identity': topics[id].uuid(),
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
