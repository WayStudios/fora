# fora
# class ThreadView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.thread import Thread

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPForbidden
)

class ThreadView(View):
    """ This class contains the thread view of fora.
    """
    def __init__(self, request):
        super(ThreadView, self).__init__(request = request,
                                        template = 'fora:templates/thread.pt',
                                        actions = {
                                        })
        self.title = 'Thread'
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        thread = Thread.get_thread_by_uuid(uuid = self.value['identity'])
        if not thread:
            self.exception = HTTPNotFound()
        else:
            self.title = 'Thread ' + thread.subject()
            self.value['thread'] = {
                'author': thread.author(),
                'subject': thread.subject(),
                'content': thread.content(),
                'create_date': thread.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': thread.update_date().strftime('%Y-%m-%d %H:%M:%S')
            }
        super(ThreadView, self).prepare_template()
