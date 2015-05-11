import os

from pyramid.scaffolds.template import Template # API

class ForaTemplate(Template):
    def pre(self, command, output_dir, vars):
        return Template.pre(self, command, output_dir, vars)
    def post(self, command, output_dir, vars):
        return Template.post(self, command, output_dir, vars)

class GenericInstanceTemplate(ForaTemplate):
    _template_dir = 'generic'
    summary = 'fora generic instance'
