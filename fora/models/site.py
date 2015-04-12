# fora
# class SiteModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class SiteModel(Model):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    title = Column(String)
    is_active = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
