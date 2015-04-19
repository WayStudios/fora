# fora
# class ModeratorModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class ModeratorModel(Model):
    __tablename__ = 'moderators'
    id = Column(Integer, primary_key = True, autoincrement = True)
    user = Column(String, unique = True)
    password = Column(String)
    is_active = Column(Boolean)
    is_deleted = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
