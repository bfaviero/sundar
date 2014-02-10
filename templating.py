from django.http import HttpResponse
from django.template import Context, loader
from utils import log_error

"""
This class exists for two reasons.  First, to wrap django's templating.
Second, to be able to inject variables into the context before a template
is rendered. 
"""

class Template(object):
    template = None
    context = None
    
    def __init__(self, template, context={}):
        self.template = template
        self.context = context
        
    def render(self):
        template = loader.get_template(self.template)
        return HttpResponse(template.render(Context(self.context)))

def error(message):
    return HttpResponse("ERROR: " + str(message))

# TODO: improve
def error_page(message):
    return error(message)
