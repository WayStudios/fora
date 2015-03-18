# fora
# class ScoreModel
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.model import Model

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

class ScoreModel(Model):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key = True, autoincrement = True)
    uuid = Column(String, unique = True)
    scorer = Column(String)
    name = Column(String)
    value = Column(Integer)
    create_date = Column(DateTime)
    update_date = Column(DateTime)
