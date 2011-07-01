=======================
django-admin-langswitch
=======================

Adds easy language switch in admin

Installation:
-------------

* add 'admin_langswitch' to INSTALLED_APPS (after putting it on PYTHON PATH) 
* add '(r'^i18n/', include('django.conf.urls.i18n')),' to your urls.py


If you plan to use django-admin-langswitch with DjangoCMS (http://www.django-cms.org/), you should replace 'cms.middleware.multilingual.MultilingualURLMiddleware' with customised middleware. You can use 'admin_langswitch.middleware.CustomMultilingualURLMiddleware'. Please look into that module for a moment before you deploy. Of course in case you don't use DjangoCMS, this middleware is absolutely not needed.