# fora
# class AdminSitesView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.adminview import AdminView
from fora.core.site import Site

from pyramid.renderers import render_to_response

from pyramid.httpexceptions import (
    HTTPFound
)

class AdminSitesView(AdminView):
    """ This class contains the sites administration view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/sites.pt' % {'path': AdminView.path['templates']}
        super(AdminSitesView, self).__init__(request = request,
                                             template = template,
                                             actions = {
                                                 'retrieve_sites': self.retrieve_sites,
                                                 'retrieve_site': self.retrieve_site,
                                                 'delete_site': self.delete_site
                                             })
        if 'identity' in request.matchdict:
            self.identity = request.matchdict['identity']
    def prepare_template(self):
        if not self.moderator.is_guest():
            if self.activity == 'view':
                site = Site.get_site_by_uuid(self.identity)
                self.value['site'] = {
                    'uuid': site.uuid(),
                    'title': site.title(),
                    'is_active': site.is_active(),
                    'create_date': site.create_date().strftime('%Y-%m-%d %H:%M:%S'),
                    'update_date': site.update_date().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.template = '%(path)s/sites/view.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'create':
                self.template = '%(path)s/sites/create.pt' % {'path': AdminView.path['templates']}
            elif self.activity == 'edit':
                site = Site.get_site_by_uuid(self.identity)
                self.value['site'] = {
                    'uuid': site.uuid(),
                    'title': site.title(),
                    'is_active': site.is_active()
                }
                self.template = '%(path)s/sites/edit.pt' % {'path': AdminView.path['templates']}
        else:
            self.exception = HTTPFound(self.request.route_url("admin_portal"))
        super(AdminSitesView, self).prepare_template()
    def retrieve_sites(self):
        value = {
            'status': True,
            'entries': []
        }
        sites = Site.get_sites()
        for id in sites:
            value['entries'].append({
                'identity': sites[id].uuid(),
                'id': sites[id].id(),
                'title': sites[id].title(),
                'is_active': sites[id].is_active(),
                'create_date': sites[id].create_date().strftime('%Y-%m-%d %H:%M:%S'),
                'update_date': sites[id].update_date().strftime('%Y-%m-%d %H:%M:%S')
            })
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def retrieve_site(self):
        value = {
            'status': True,
            'entry': {}
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
    def delete_site(self):
        value = {
            'status': True
        }
        self.response = render_to_response(renderer_name = 'json',
                                           value = value,
                                           request = self.request)
