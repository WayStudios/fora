# fora
# class View
# Xu [xw901103@gmail.com] Copyright 2015
from pyramid.renderers import render_to_response

from fora.core.configuration import Configuration

class View(object):
    request = None
    json = None
    template = None
    value = {}
    actions = {}
    response = None
    configurations = {}
    def __init__(self, request, template, actions):
        self.request = request
        try:
            self.json = self.request.json_body
        except:
            self.json = None
        self.template = template
        self.actions = actions
    def prepare_template(self):
        self.configurations['fora_site_name'] = Configuration.get_configuration_by_name('fora_site_name')
        if self.configurations['fora_site_name']:
            self.value['fora_site_name'] = self.configurations['fora_site_name'].model.value
        else:
            self.value['fora_site_name'] = 'fora'
    def do_action(self, action):
        if action in self.actions:
            self.actions[action]()
    def __call__(self):
        if 'action' in self.request.GET:
            self.do_action(self.request.GET['action'])
        else:
            self.prepare_template()
            self.response = render_to_response(renderer_name = self.template,
                                               value = self.value,
                                               request = self.request)
        return self.response
    def __name__(self):
        return self.name
