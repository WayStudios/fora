# fora
# class PageModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

class PageModel(Model):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    title = Column(String)
    description = Column(String)
    content = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
