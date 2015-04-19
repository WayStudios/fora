# fora
# class Moderator
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.dbsession import (
    DBSession,
    OR
)

class Moderator(object):
    """ This class contains core functionality of fora moderator manipulation.
    """
    model = None
    def __init__(self):
        self.model = None
    def exists(self):
        return self.model != None
