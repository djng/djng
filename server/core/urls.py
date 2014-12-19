# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from static import client_static
from core.admin import admin_site


urlpatterns = patterns('',
                       url(r'^admin/', include(admin_site.urls)),
                       url(r'^api/', include('api.urls')))

# Add client urls for debug mode
urlpatterns += client_static()

# This catch all url has to be last
urlpatterns += url(r'^.*$', 'core.views.home', name='home'),
