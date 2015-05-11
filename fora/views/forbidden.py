# fora
# class ForbiddenView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

class ForbiddenView(View):
    """ This class contains the 403 forbidden view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/forbidden.pt' % {'path': View.path['templates']}
        super(ForbiddenView, self).__init__(request = request,
                                            template = template,
                                            actions = {
                                            })
        self.title = self.localizer.translate('403 Forbidden', domain = 'fora')
