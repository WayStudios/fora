# fora
# class TopicView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.topic import Topic

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPForbidden
)

class TopicView(View):
    """ This class contains the topic view of fora.
    """
    def __init__(self, request):
        super(TopicView, self).__init__(request = request,
                                        template = 'fora:templates/topic.pt',
                                        actions = {
                                            'retrieve_threads': self.retrieve_threads,
                                            'reply_topic': self.reply_topic,
                                            'edit_thread': self.edit_thread,
                                            'delete_thread': self.delete_thread
                                        })
        self.title = self.localizer.translate('Topic', domain = 'fora')
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        topic = Topic.get_topic_by_uuid(uuid = self.value['identity'])
        if not topic:
            self.exception = HTTPNotFound()
        else:
            self.title = self.localizer.translate('Topic ${topic_subject}', domain = 'fora', mapping = {'topic_subject': topic.subject()})
            self.value['topic'] = {
                'subject': topic.subject()
            }
        super(TopicView, self).prepare_template()
    def retrieve_threads(self):
        value = {
            'status': True,
            'entries': {}
        }
        topic = Topic.get_topic_by_uuid(uuid = self.value['identity'])
        threads = topic.get_threads()
        for uuid in threads:
            thread = threads[uuid]
            value['entries'][uuid] = {
                'id': thread.id(),
                'uuid': thread.uuid(),
                'author': thread.author(),
                'subject': thread.subject(),
                'content': thread.content(),
                'create_date': thread.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': thread.update_date().strftime('%Y-%m-%d %H:%M:%S')
            }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def reply_topic(self):
        value = {
            'status': True,
            'uuid': ''
        }
        subject = self.json['subject']
        content = self.json['content']
        topic = Topic.get_topic_by_uuid(uuid = self.value['identity'])
        thread = topic.create_thread(author = 'anonymous', subject = subject, content = content)
        value['uuid'] = thread.uuid()
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def edit_thread(self):
        value = {
            'status': True
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
