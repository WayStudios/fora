# fora
# class UserModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    DateTime
)

class UserModel(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    email = Column(String, unique = True)
    username = Column(String, unique = True)
    password = Column(String)
    is_active = Column(Boolean)
    is_deleted = Column(Boolean)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
