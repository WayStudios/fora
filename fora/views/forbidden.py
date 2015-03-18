# fora
# class ForbiddenView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

class ForbiddenView(View):
    """ This class contains the 403 forbidden view of fora.
    """
    def __init__(self, request):
        super(ForbiddenView, self).__init__(request = request,
                                            template = 'fora:templates/forbidden.pt',
                                            actions = {
                                            })
