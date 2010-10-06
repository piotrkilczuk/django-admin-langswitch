from django.conf import settings
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.utils import translation

class CustomMultilingualURLMiddleware(MultilingualURLMiddleware, object):
    """
    Supplies additional method that redirects / to /pl /en /de etc.
    
    This class is EXPERIMENTAL although working successfully in production environment.
    Please take  a moment to examine/adapt the code, to make sure it does what you need.
    """
    
    from cms.middleware.multilingual import MultilingualURLMiddleware
    
    def is_cms(self, request):
        try:
            func = urlresolvers.resolve(request.path)[0]
            func_full_name = ('.').join((func.__module__, func.__name__))
            return func_full_name.startswith('cms')
        except AttributeError:
            return False
        except urlresolvers.Resolver404:
            return None
    
    def process_request(self, request):
        if self.is_cms(request):
            language = self.get_language_from_request(request)
        else:
            language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = language
        if request.META['PATH_INFO'] == '/' and settings.CMS_SEO_ROOT:
            return HttpResponseRedirect('/%s/' % language)
    
    def process_response(self, request, response):
        if self.is_cms(request):
            return super(CustomMultilingualURLMiddleware, self).process_response(request, response)
        else:
            return response