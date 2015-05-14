# fora
# class ForumView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.forum import Forum
from fora.core.thread import Thread

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPForbidden
)

from ipaddress import ip_address
from hashids import Hashids

class ForumView(View):
    """ This class contains the forum view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/forum.pt' % {'path': View.path['templates']}
        super(ForumView, self).__init__(request = request,
                                        template = template,
                                        actions = {
                                            'retrieve_forums': self.retrieve_forums,
                                            'retrieve_topics': self.retrieve_topics,
                                            'create_topic': self.create_topic,
                                            'delete_topic': self.delete_topic
                                        })
        self.title = self.localizer.translate('Forum', domain = 'fora')
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        forum = Forum.get_forum_by_uuid(self.value['identity'])
        if not forum:
            self.exception = HTTPNotFound()
        else:
            self.title = self.localizer.translate('Forum ${forum_title}', domain = 'fora', mapping = {'forum_title': forum.title()})
            self.value['forum'] = {
                'title': forum.title(),
                'description': forum.description()
            }
        super(ForumView, self).prepare_template()
    def retrieve_forums(self):
        value = {
            'status': True,
            'length': 0,
            'entries': {}
        }
        forums = Forum.get_forums_by_parent(parent = self.value['identity'])
        for id in forums:
            if forums[id].is_active() and not forums[id].is_deleted():
                value['entries'][id] = {
                    'uuid': forums[id].uuid(),
                    'title': forums[id].title(),
                    'description': forums[id].description()
                }
                value['length'] += 1
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_topics(self):
        value = {
            'status': True,
            'length': 0,
            'entries': {}
        }
        forum = Forum.get_forum_by_uuid(uuid = self.value['identity'])
        topics = forum.get_topics()
        for id in topics:
            thread = Thread.get_thread_by_uuid(uuid = topics[id].initial_thread())
            value['entries'][id] = {
                'uuid': topics[id].uuid(),
                'initial_thread': {
                    'uuid': thread.uuid(),
                    'author': thread.author(),
                    'subject': thread.subject()
                }
            }
            value['length'] += 1
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def create_topic(self):
        value = {
            'status': True,
            'uuid': '',
        }
        subject = self.json['subject']
        content = self.json['content']
        author = 'anonymous'
        is_anonymous = True
        if self.user.is_guest():
            hashids = Hashids(salt = 'fora')
            remote_addr = ip_address(self.request.remote_addr).packed
            author = hashids.encode(int(remote_addr[0]),
                                    int(remote_addr[1]),
                                    int(remote_addr[2]),
                                    int(remote_addr[3]))
        else:
            author = self.user.uuid()
            is_anonymous = False
        forum = Forum.get_forum_by_uuid(self.value['identity'])
        topic = forum.create_topic(author = author, subject = subject, content = content, is_anonymous = is_anonymous)
        value['uuid'] = topic.uuid()
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
