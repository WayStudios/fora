# fora
# class AdminView
# Xu [xw901103@gmail.com] Copyright 2015
from pyramid.renderers import render_to_response

from fora.core.configuration import Configuration
from fora.core.user import User

class AdminView(object):
    """ This class contains the general administration view object functionality of fora.
    """
    path = {
        'static': '',
        'templates': ''
    }
    title = None
    request = None
    session = None
    moderator = None
    exception = None
    json = None
    template = None
    localizer = None
    value = {}
    activity = None
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
        if 'activity' in request.matchdict:
            self.activity = request.matchdict['activity']
    def do_action(self, action):
        if action in self.actions:
            self.actions[action]()
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
            'is_guest': self.moderator.is_guest()
        }
        if not self.moderator.is_guest():
            self.value['session']['uuid'] = self.moderator.uuid()
            self.value['session']['username'] = self.moderator.username()
    def __call__(self):
        if 'moderator' in self.session:
            self.moderator = User.get_user_by_identity(self.session['moderator'])
        if not self.moderator:
            self.moderator = User()
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
