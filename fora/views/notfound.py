# fora
# class NotFoundView
# Xu [xw901103@gmail.com] Copyright 2015
from fora.core.view import View

class NotFoundView(View):
    """ This class contains the 404 not found view of fora.
    """
    def __init__(self, request):
        template = '%(path)s/notfound.pt' % {'path': View.path['templates']}
        super(NotFoundView, self).__init__(request = request,
                                           template = template,
                                           actions = {
                                           })
        self.title = self.localizer.translate('404 Not Found', domain = 'fora')
