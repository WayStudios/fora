# fora
# class NotFoundView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

class NotFoundView(View):
    """ This class contains the 404 not found view of fora.
    """
    def __init__(self, request):
        super(NotFoundView, self).__init__(request = request,
                                           template = 'fora:templates/notfound.pt',
                                           actions = {
                                           })
