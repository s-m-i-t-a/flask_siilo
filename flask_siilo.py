# -*- coding: utf-8 -*-

__author__ = 'Jindřich Smitka'
__email__ = 'smitka.j@gmail.com'
__version__ = '0.1.0'

import six
import sys

from importlib import import_module

from flask import current_app

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


def import_string(dotted_path):
    try:
        module_path, cls_name = dotted_path.rsplit('.', 1)
    except ValueError:
        six.reraise(ImportError, ImportError("Doesn't look like a module path"), sys.exc_info()[2])

    module = import_module(module_path)

    try:
        return getattr(module, cls_name)
    except AttributeError:
        msg = 'Module does not define a "%s"' % cls_name
        six.reraise(ImportError, ImportError(msg), sys.exc_info()[2])


class Storage(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SIILO_STORAGE_CLASS',
                              'siilo.storages.filesystem.FileSystemStorage')

    @property
    def storage(self):
        pass
