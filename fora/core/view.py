# fora
# class View
# Xu [xw901103@gmail.com] Copyright 2015
from pyramid.renderers import render_to_response

from fora.core.configuration import Configuration
from fora.core.user import User

class View(object):
    """ This class contains the general view object functionality of fora.
    """
    path = {
        'static': '',
        'templates': ''
    }
    title = None
    request = None
    session = None
    user = None
    exception = None
    json = None
    template = None
    localizer = None
    value = {}
    actions = {}
    response = None
    configurations = {}
    def __init__(self, request, template, actions):
        self.request = request
        self.session = request.session
        self.localizer = request.localizer
        try:
            self.json = request.json_body
        except:
            self.json = None
        self.template = template
        self.value['path'] = self.path
        self.actions = actions
    def prepare_template(self):
        self.configurations['fora_site_name'] = Configuration.get_configuration_by_name('fora_site_name')
        if self.configurations['fora_site_name']:
            self.value['fora_site_name'] = self.configurations['fora_site_name'].model.value
        else:
            self.value['fora_site_name'] = 'fora'
        if not self.title:
            self.value['title'] = self.value['fora_site_name']
        else:
            self.value['title'] = self.value['fora_site_name'] + ' - ' + self.title
        self.value['session'] = {
            'uuid': 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx',
            'username': 'anonymous',
            'is_guest': self.user.is_guest()
        }
        if not self.user.is_guest():
            self.value['session']['uuid'] = self.user.uuid()
            self.value['session']['username'] = self.user.username()
    def do_action(self, action):
        if action in self.actions:
            self.actions[action]()
    def __call__(self):
        if 'user' in self.session:
            self.user = User.get_user_by_identity(self.session['user'])
        if not self.user:
            self.user = User()
        if 'action' in self.request.GET:
            self.do_action(self.request.GET['action'])
        else:
            self.prepare_template()
            if self.exception:
                raise self.exception
            self.response = render_to_response(renderer_name = self.template,
                                               value = self.value,
                                               request = self.request)
        return self.response
    def __name__(self):
        return self.name
