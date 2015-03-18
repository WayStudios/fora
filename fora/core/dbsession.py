# fora
# class DBSession
# Xu [xw901103@gmail.com] Copyright 2015
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from sqlalchemy import (
    asc,
    desc
)
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
ASC = asc
DESC = desc
