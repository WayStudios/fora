# fora
# class ConfigurationModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

class ConfigurationModel(Model):
    __tablename__ = 'configurations'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    type = Column(String)
    name = Column(String)
    value = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
