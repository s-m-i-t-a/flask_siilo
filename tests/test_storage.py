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
        app = Flask(__name__)
        storage = Storage(app)

        from siilo.storages.filesystem import FileSystemStorage
        assert isinstance(storage.storage, FileSystemStorage)


class TestImportFromString(object):
    def test_import_class_from_string(self):
        cls = import_string('siilo.storages.filesystem.FileSystemStorage')

        from siilo.storages.filesystem import FileSystemStorage
        assert cls == FileSystemStorage
