# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from core.admin import admin_site

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^admin/', include(admin_site.urls)),
    url(r'^api/', include('api.urls'))
)
