# fora
# class InstallView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

class InstallView(View):
    """ This class contains the install view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/install.pt' % {'path': View.path['templates']}
        super(InstallView, self).__init__(request = request,
                                          template = template,
                                          actions = {
                                              'start_installation': self.start_installation
                                          })
        self.title = self.localizer.translate('Install', domain = 'fora')
    def prepare_template(self):
        super(InstallView, self).prepare_template()
    def start_installation(self):
        return
