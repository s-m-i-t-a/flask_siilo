# -*- coding: utf-8 -*-

__author__ = 'Jindřich Smitka'
__email__ = 'smitka.j@gmail.com'
__version__ = '0.1.1'

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
    def __init__(self, app=None, name='default'):
        self.app = app
        self.name = name
        self.ctx_storage_name = '%s_storage' % name
        self.storage_class_name = '%s_STORAGE_CLASS' % name.upper()
        self.storage_settings_name = '%s_STORAGE_SETTINGS' % name.upper()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault(self.storage_class_name,
                              'siilo.storages.filesystem.FileSystemStorage')

    @property
    def storage(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, self.ctx_storage_name):
                storage_class = import_string(current_app.config[self.storage_class_name])
                setattr(ctx, self.ctx_storage_name, storage_class(**current_app.config[self.storage_settings_name]))

            return getattr(ctx, self.ctx_storage_name)
