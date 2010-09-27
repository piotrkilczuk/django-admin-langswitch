from django.conf import settings
from django.core import urlresolvers
from django.core.exceptions import ImproperlyConfigured
import os.path

URL = ''

# check if 'django.views.i18n.set_language' is reachable via url, otherwise raise ImproperlyConfigured
# this does not work for some reason when running in Apache/WSGI environment (threading issues?)
# disabled for further research

#try:
#    URL = urlresolvers.reverse('django.views.i18n.set_language')
#except urlresolvers.NoReverseMatch:
#    raise ImproperlyConfigured('Cannot resolve django.views.i18n.set_language to URL - see http://docs.djangoproject.com/en/1.2/topics/i18n/internationalization/#the-set-language-redirect-view')

# register additional template dir
HERE = os.path.abspath(os.path.dirname(__file__))
settings.TEMPLATE_DIRS += (os.path.join(HERE, 'templates'),)

# @todo: Add ctx processor which adds Template object to the context
#        This way it will be possible for admin/base.html to extend admin/base.html from 
#        django.contrib.admin
#
#        Another approach may be to write custom extension tag, which would make it possible
#        to specify which exact app to use for finding parent tpl. Ex.:
#        {% extendsfrom 'temp/late.html' 'django.contrib.admin' %}