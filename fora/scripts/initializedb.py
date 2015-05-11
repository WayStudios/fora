import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from fora.core.dbsession import DBSession
from fora.core.model import Model
from fora.models.configuration import ConfigurationModel
from fora.models.user import UserModel
from fora.models.moderator import ModeratorModel
from fora.models.site import SiteModel
from fora.models.forum import ForumModel
from fora.models.topic import TopicModel
from fora.models.thread import ThreadModel
from fora.models.article import ArticleModel
from fora.models.property import PropertyModel
from fora.models.score import ScoreModel

from fora.models.siteforum import SiteForumModel
from fora.models.forumtopic import ForumTopicModel
from fora.models.topicthread import TopicThreadModel

import uuid
from datetime import datetime

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Model.metadata.create_all(engine)
    with transaction.manager:
        user_uuid = str(uuid.uuid4())
        site_uuid = str(uuid.uuid4())
        forum_uuid = str(uuid.uuid4())
        thread_uuid = str(uuid.uuid4())
        topic_uuid = str(uuid.uuid4())
        conf_fora_site_name = ConfigurationModel(uuid = str(uuid.uuid4()), type = 'string', name = 'fora_site_name', value = 'fora', create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(conf_fora_site_name)
        user_fora_admin = UserModel(uuid = user_uuid, email_address = 'admin@fora.io', username = 'admin', password = 'admin', is_active = True, is_deleted = False, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(user_fora_admin)
        moderator_fora_admin = ModeratorModel(user = user_uuid, password = 'admin', is_active = True, is_deleted = False, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(moderator_fora_admin)
        site_fora_demo = SiteModel(uuid = site_uuid, title = 'fora', is_active = True, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(site_fora_demo)
        forum_fora_demo = ForumModel(uuid = forum_uuid, title = 'Demo', description = 'A demo forum', is_active = True, is_deleted = False, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(forum_fora_demo)
        article_fora_about = ArticleModel(uuid = str(uuid.uuid4()), title = 'About', description = 'CMS about page', content = 'This is the about page.', is_active = True, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(article_fora_about)
        article_fora_contact = ArticleModel(uuid = str(uuid.uuid4()), title = 'Contact', description = 'CMS contact page', content = 'This is the contact page.', is_active = True, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(article_fora_contact)
        thread_fora_demo = ThreadModel(uuid = thread_uuid, parent = thread_uuid, author = 'anonymous', subject = 'demo', content = 'demo content', is_anonymous = True, is_archived = False, is_deleted = False, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(thread_fora_demo)
        topic_fora_demo = TopicModel(uuid = topic_uuid, initial_thread = thread_uuid, is_archived = False, is_deleted = False, create_date = datetime.utcnow(), update_date = datetime.utcnow())
        DBSession.add(topic_fora_demo)
        topicthread_fora_demo = TopicThreadModel(topic = topic_uuid, thread = thread_uuid)
        DBSession.add(topicthread_fora_demo)
        forumtopic_fora_demo = ForumTopicModel(forum = forum_uuid, topic = topic_uuid)
        DBSession.add(forumtopic_fora_demo)
