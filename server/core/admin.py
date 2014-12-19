# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class BaseAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = BaseAdminSite()
