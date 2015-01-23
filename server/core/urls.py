# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from core.admin import admin_site


urlpatterns = patterns('',
                       url(r'^admin/', include(admin_site.urls)),
                       url(r'^api/', include('api.urls')))

# Add client urls for debug mode
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# This catch all url has to be last
urlpatterns += url(r'^.*$', 'core.views.home', name='home'),
