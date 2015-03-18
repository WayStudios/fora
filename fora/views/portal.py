# fora
# class PortalView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View
from fora.core.forum import Forum

from pyramid.renderers import render_to_response

class PortalView(View):
    """ This class contains the home portal view of fora.
    """
    def __init__(self, request):
        super(PortalView, self).__init__(request = request,
                                         template = 'fora:templates/portal.pt',
                                         actions = {
                                             'retrieve_forums': self.retrieve_forums
                                         })
    def prepare_template(self):
        super(PortalView, self).prepare_template()
    def retrieve_forums(self):
        value = {
            'status': True,
            'entries': {}
        }
        forums = Forum.get_forums()
        for uuid in forums:
            value['entries'][uuid] = {
                'uuid': uuid,
                'title': forums[uuid].title(),
                'description': forums[uuid].description()
            }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
