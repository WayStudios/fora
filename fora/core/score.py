# fora
# class Score
# Xu [xw901103@gmail.com] Copyright 2015

class Score(object):
    """ This class contains core functionality of fora score manipulation.
    """
    model = None
    def __init__(self):
        self.model = None
    def id(self):
        return self.model.id
    def uuid(self, new_uuid = None):
        if not new_uuid:
            return self.model.uuid
        self.model.uuid = new_uuid
    def scorer(self, new_scorer = None):
        if not new_scorer:
            return self.model.scorer
        self.model.scorer = new_scorer
    def name(self, new_name = None):
        if not new_name:
            return self.model.name
        self.model.name = new_name
    def value(self, new_value = None):
        if not new_value:
            return self.model.value
        self.model.value = new_value
    def create_date(self, new_create_date = None):
        if not new_create_date:
            return self.model.create_date
        self.model.create_date = new_create_date
    def update_date(self, new_update_date = None):
        if not new_update_date:
            return self.model.update_date
        self.model.update_date = new_update_date
