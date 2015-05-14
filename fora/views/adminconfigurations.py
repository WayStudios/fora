# fora
# class AdminConfigurationsView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.configuration import Configuration

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminConfigurationsView(AdminView):
    """ This class contains the configurations administration view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/configurations.pt' % {'path': AdminView.path['templates']}
        super(AdminConfigurationsView, self).__init__(request = request,
                                                      template = template,
                                                      actions = {
                                                          'retrieve_configurations': self.retrieve_configurations,
                                                          'retrieve_configuration': self.retrieve_configuration,
                                                          'delete_configuration': self.delete_configuration
                                                      })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                configuration = Configuration.get_configuration_by_uuid(self.identity)
                self.value['configuration'] = {
                    'uuid': configuration.uuid(),
                    'type': configuration.type(),
                    'name': configuration.name(),
                    'value': configuration.value(),
                    'create_date': configuration.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': configuration.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/configurations/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/configurations/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                configuration = Configuration.get_configuration_by_uuid(self.identity)
                self.value['configuration'] = {
                    'uuid': configuration.uuid(),
                    'type': configuration.type(),
                    'name': configuration.name(),
                    'value': configuration.value()
                }
                self.template = '%(path)s/configurations/edit.pt' % {'path': AdminView.path['templates']}
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminConfigurationsView, self).prepare_template()
    def retrieve_configurations(self):
        value = {
            'status': True,
            'entries': []
        }
        configurations = Configuration.get_configurations()
        for id in configurations:
            value['entries'].append({
                'identity': configurations[id].uuid(),
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
