# fora
# class AdminConfigurationsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.configuration import Configuration

from pyramid.renderers import render_to_response

class AdminConfigurationsView(View):
    """ This class contains the configurations administration view of fora.
    """
    def __init__(self, request):
        super(AdminConfigurationsView, self).__init__(request = request,
                                                      template = 'fora:templates/admin/configurations.pt',
                                                      actions = {
                                                          'retrieve_configurations': self.retrieve_configurations,
                                                          'retrieve_configuration': self.retrieve_configuration,
                                                          'delete_configuration': self.delete_configuration
                                                      })
    def retrieve_configurations(self):
        value = {
            'status': True,
            'entries': []
        }
        configurations = Configuration.get_configurations()
        for id in configurations:
            value['entries'].append({
                'id': configurations[id].id(),
                'type': configurations[id].type(),
                'name': configurations[id].name(),
                'value': configurations[id].value(),
                'create_date': configurations[id].create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': configurations[id].update_date().strftime('%Y-%m-%d %H:%M:%S')
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_configuration(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_configuration(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
