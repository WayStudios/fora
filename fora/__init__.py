# fora
# Xu [xw901103@gmail.com] Copyright 2015
from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from fora.core.dbsession import DBSession
from fora.core.model import Model

from fora.views.install import InstallView

from fora.views.notfound import NotFoundView

from fora.views.portal import PortalView
from fora.views.user import UserView
from fora.views.user_registration import UserRegistrationView
from fora.views.forum import ForumView
from fora.views.topic import TopicView
from fora.views.thread import ThreadView
from fora.views.page import PageView
from fora.views.admin import AdminView

import uuid

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind = engine)
    Model.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age = 3600)
    config.add_notfound_view(view = NotFoundView)
    config.add_route('install', '/install')
    config.add_view(view = InstallView, route_name = 'install')
    config.add_route('portal', '/')
    config.add_view(view = PortalView, route_name = 'portal')
    config.add_route('user_registration', '/user/register')
    config.add_view(view = UserRegistrationView, route_name = 'user_registration')
    config.add_route('user', '/user/{identity:.*}')
    config.add_view(view = UserView, route_name = 'user')
    config.add_route('forum', '/forum/{identity:.*}')
    config.add_view(view = ForumView, route_name = 'forum')
    config.add_route('topic', '/topic/{identity:.*}')
    config.add_view(view = TopicView, route_name = 'topic')
    config.add_route('thread', '/thread/{identity:.*}')
    config.add_view(view = ThreadView, route_name = 'thread')
    config.add_route('page', '/page/{identity:.*}')
    config.add_view(view = PageView, route_name = 'page')
    config.add_route('admin', '/admin')
    config.add_view(view = AdminView, route_name = 'admin')
    config.scan()
    return config.make_wsgi_app()
