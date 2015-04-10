# fora
# Xu [xw901103@gmail.com] Copyright 2015
from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from fora.core.dbsession import DBSession
from fora.core.model import Model

from fora.views.install import InstallView

from fora.views.notfound import NotFoundView
from fora.views.forbidden import ForbiddenView

from fora.views.portal import PortalView
from fora.views.user import UserView
from fora.views.registration import RegistrationView
from fora.views.forum import ForumView
from fora.views.topic import TopicView
from fora.views.thread import ThreadView
from fora.views.article import ArticleView

from fora.views.adminportal import AdminPortalView
from fora.views.admindashboard import AdminDashboardView
from fora.views.adminsites import AdminSitesView
from fora.views.adminusers import AdminUsersView
from fora.views.adminforums import AdminForumsView
from fora.views.admintopics import AdminTopicsView
from fora.views.adminthreads import AdminThreadsView
from fora.views.adminarticles import AdminArticlesView

import uuid

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind = engine)
    Model.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age = 3600)
    config.add_forbidden_view(view = ForbiddenView)
    config.add_notfound_view(view = NotFoundView)
    config.add_route('install', '/install')
    config.add_view(view = InstallView, route_name = 'install')
    config.add_route('portal', '/')
    config.add_view(view = PortalView, route_name = 'portal')
    config.add_route('registration', '/user/register')
    config.add_view(view = RegistrationView, route_name = 'registration')
    config.add_route('user', '/user/{identity:.*}')
    config.add_view(view = UserView, route_name = 'user')
    config.add_route('forum', '/forum/{identity:.*}')
    config.add_view(view = ForumView, route_name = 'forum')
    config.add_route('topic', '/topic/{identity:.*}')
    config.add_view(view = TopicView, route_name = 'topic')
    config.add_route('thread', '/thread/{identity:.*}')
    config.add_view(view = ThreadView, route_name = 'thread')
    config.add_route('article', '/article/{identity:.*}')
    config.add_view(view = ArticleView, route_name = 'article')
    config.add_route('admin_portal', '/admin')
    config.add_view(view = AdminPortalView, route_name = 'admin_portal')
    config.add_route('admin_dashboard', '/admin/dashboard')
    config.add_view(view = AdminDashboardView, route_name = 'admin_dashboard')
    config.add_route('admin_sites', '/admin/sites')
    config.add_view(view = AdminSitesView, route_name = 'admin_sites')
    config.add_route('admin_users', '/admin/users')
    config.add_view(view = AdminUsersView, route_name = 'admin_users')
    config.add_route('admin_forums', '/admin/forums')
    config.add_view(view = AdminForumsView, route_name = 'admin_forums')
    config.scan()
    return config.make_wsgi_app()
