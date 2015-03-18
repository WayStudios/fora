# fora
# class PropertyModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

class PropertyModel(Model):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    owner = Column(String)
    name = Column(String)
    type = Column(String)
    description = Column(String)
    content = Column(String)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
