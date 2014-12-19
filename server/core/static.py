# -*- coding: utf-8 -*-
import os

from dj_static import Cling
from django.conf import settings
from django.conf.urls.static import static
from django.core.handlers.wsgi import get_path_info


class SPACling(Cling):
    def __init__(self, application, base_dir=None):
        super(SPACling, self).__init__(application, base_dir=base_dir)
        self.static_prefixes = [self.base_url[2]]
        self.static_prefixes.extend(['/' + folder for folder in settings.CLIENT_ASSET_DIRS])
        self.static_prefixes = tuple(self.static_prefixes)

    def _transpose_environ(self, environ):
        """
        Translates a given environ to static.Cling's expectations
        for base_url (STATIC_URL) only.
        """
        if get_path_info(environ).startswith(self.base_url[2]):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.base_url[2]) - 1:]
        return environ

    def _should_handle(self, path):
        """
        Checks if the path should be handled.
        """
        return path.startswith(self.static_prefixes)


def client_static():
    """
    Helper function to return a URL pattern for serving files in debug mode.
    :rtype: list
    """
    # No-op if not in debug mode
    if not settings.DEBUG:
        return []

    urlpatterns = []

    for folder in settings.CLIENT_ASSET_DIRS:
        # ignore source css folder as it gets compiled by compass into the tmp dir
        if folder == 'styles':
            continue
        urlpatterns += static(folder, document_root=os.path.join(settings.CLIENT_BASE_DIR, 'app', folder))

    urlpatterns += static('bower_components',
                          document_root=os.path.join(settings.CLIENT_BASE_DIR, 'bower_components'))
    urlpatterns += static('styles', document_root=os.path.join(settings.CLIENT_BASE_DIR, '.tmp/styles'))

    return urlpatterns
