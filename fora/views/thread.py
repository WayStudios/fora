# fora
# class ThreadView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.thread import Thread
from fora.core.user import User

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPForbidden
)

class ThreadView(View):
    """ This class contains the thread view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/thread.pt' % {'path': View.path['templates']}
        super(ThreadView, self).__init__(request = request,
                                        template = template,
                                        actions = {
                                        })
        self.title = self.localizer.translate('Thread', domain = 'fora')
        self.value['identity'] = request.matchdict['identity']
    def prepare_template(self):
        thread = Thread.get_thread_by_uuid(uuid = self.value['identity'])
        if not thread:
            self.exception = HTTPNotFound()
        else:
            self.title = self.localizer.translate('Thread ${thread_subject}', domain = 'fora', mapping = {'thread_subject': thread.subject()})
            self.value['thread'] = {
                'id': thread.id(),
                'is_anonymous': True,
                'author': thread.author(),
                'username': thread.author(),
                'subject': thread.subject(),
                'content': thread.content(),
                'create_date': thread.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': thread.update_date().strftime('%Y-%m-%d %H:%M:%S')
            }
            if not thread.is_anonymous():
                user = User.get_user_by_identity(thread.author())
                if not user.is_guest():
                    self.value['thread']['is_anonymous'] = False
                    self.value['thread']['username'] = user.username()
        super(ThreadView, self).prepare_template()
