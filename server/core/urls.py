# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy

admin.site.site_title = ugettext_lazy('My site admin')
admin.site.site_header = ugettext_lazy('My administration')
admin.site.index_title = ugettext_lazy('Site administration')

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include('api.urls')))

# Add client urls for debug mode
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# This catch all url has to be last
urlpatterns += url(r'^.*$', 'core.views.home', name='home'),
