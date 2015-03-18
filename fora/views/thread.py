# fora
# class ThreadView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.thread import Thread

from pyramid.renderers import render_to_response

class ThreadView(View):
    """ This class contains the thread view of fora.
    """
    def __init__(self, request):
        super(ThreadView, self).__init__(request = request,
                                        template = 'fora:templates/thread.pt',
                                        actions = {
                                        })
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        super(ThreadView, self).prepare_template()
        self.value['thread'] = {
            'author': '',
            'subject': '',
            'content': '',
            'create_date': '',
            'update_date': ''
        }
        thread = Thread.get_thread_by_uuid(uuid = self.value['identity'])
        self.value['thread']['author'] = thread.author()
        self.value['thread']['subject'] = thread.subject()
        self.value['thread']['content'] = thread.content()
        self.value['thread']['create_date'] = str(thread.create_date())
        self.value['thread']['update_date'] = str(thread.update_date())
