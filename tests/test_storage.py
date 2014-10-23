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

    def test_two_different_storages(self):
        default_settings = {
            'base_directory': '/tmp',
        }

        s3_settings = {
            'access_key_id': 'your access key id',
            'secret_access_key': 'your secret access key',
            'bucket': 'example-bucket'
        }

        app = Flask(__name__)
        app.config.setdefault('DEFAULT_STORAGE_SETTINGS', default_settings)
        app.config.setdefault('S3_STORAGE_SETTINGS', s3_settings)
        app.config.setdefault('S3_STORAGE_CLASS', 'siilo.storages.amazon_s3.AmazonS3Storage')

        s = Storage(app)
        s3 = Storage(app, 's3')

        ctx = app.app_context()
        ctx.push()
        default_storage = s.storage
        s3_storage = s3.storage
        ctx.pop()

        from siilo.storages.filesystem import FileSystemStorage
        assert isinstance(default_storage, FileSystemStorage)

        from siilo.storages.amazon_s3 import AmazonS3Storage
        assert isinstance(s3_storage, AmazonS3Storage)


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
