# fora
# class InstallView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

class InstallView(View):
    """ This class contains the install view of fora.
    """
    def __init__(self, request):
        super(InstallView, self).__init__(request = request,
                                          template = 'fora:templates/install.pt',
                                          actions = {
                                              'start_installation': self.start_installation
                                          })
    def start_installation(self):
        return