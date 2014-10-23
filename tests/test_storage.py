# -*- coding: utf-8 -*-

import six
import pytest


if six.PY3:
    from unittest.mock import patch, call
else:
    from mock import patch, call

from flask import Flask

from flask_siilo import Storage, import_string


class TestStorage(object):
    def test_return_local_file_storage_as_default_storage(self):
        settings = {
            'base_directory': '/tmp',
        }
        app = Flask(__name__)
        app.config.setdefault('DEFAULT_STORAGE_SETTINGS', settings)
        s = Storage(app)

        ctx = app.app_context()
        ctx.push()
        storage = s.storage
        ctx.pop()

        from siilo.storages.filesystem import FileSystemStorage
        assert isinstance(storage, FileSystemStorage)


class TestImportFromString(object):
    def test_import_class_from_string(self):
        cls = import_string('siilo.storages.filesystem.FileSystemStorage')

        from siilo.storages.filesystem import FileSystemStorage
        assert cls == FileSystemStorage

    def test_raise_import_error_when_string_is_not_dotted_path(self):
        with pytest.raises(ImportError):
            import_string('hokus pokus')

    def test_raise_import_error_when_class_or_attribute_not_found(self):
        with pytest.raises(ImportError):
            import_string('siilo.storages.filesystem.FooBarBaz')
