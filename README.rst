===============================
Flask-Siilo
===============================

.. image:: https://badge.fury.io/py/flask_siilo.png
    :target: http://badge.fury.io/py/flask_siilo

.. image:: https://travis-ci.org/s-m-i-t-a/flask_siilo.png?branch=master
        :target: https://travis-ci.org/s-m-i-t-a/flask_siilo

.. image:: https://pypip.in/d/flask_siilo/badge.png
        :target: https://pypi.python.org/pypi/flask_siilo

.. image:: https://coveralls.io/repos/s-m-i-t-a/flask_siilo/badge.png
        :target: https://coveralls.io/r/s-m-i-t-a/flask_siilo

.. image:: https://requires.io/github/s-m-i-t-a/flask_siilo/requirements.svg?branch=master
        :target: https://requires.io/github/s-m-i-t-a/flask_siilo/requirements/?branch=master
        :alt: Requirements Status


A simple storage for Flask.

Free software: BSD license

Quickstart
----------
Install flask_siilo::

    pip install flask_siilo

In the app you must init the ``Storage``::

    from flask import Flask
    from flask.ext.siilo import Storage

    app = Flask(__name__)
    storage = Storage(app)

As default is used ``siilo.storages.filesystem.FileSystemStorage`` and you must set ``DEFAULT_STORAGE_SETTINGS`` as dict with ``base_directory`` keyword::

    app.config['DEFAULT_STORAGE_SETTINGS'] = {
        'base_directory': '/foo/bar/baz',
    }


Multiple storages
-----------------

For use with multiple storages you must set name on storage class::

    from flask import Flask
    from flask.ext.siilo import Storage

    app = Flask(__name__)
    default_storage = Storage(app)
    foo_storage = Storage(app, name='foo')

and set ``FOO_STORAGE_SETTINGS``::

    app.config['FOO_STORAGE_SETTINGS'] = {
        'base_directory': '/foo/bar',
    }


Settings
--------

Storage classes
===============

DEFAULT_STORAGE_CLASS (or SOMETHING_STORAGE_CLASS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * ``siilo.storages.amazon_s3.AmazonS3Storage``
    * ``siilo.storages.filesystem.FileSystemStorage``

DEFAULT_STORAGE_SETTINGS (or SOMETHING_STORAGE_SETTINGS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    * `AmazonS3Storage (Paramteres section)`_
    * `FileSystemStorage (Paramteres section)`_

.. _AmazonS3Storage (Paramteres section): http://siilo.readthedocs.org/storages/amazon_s3.html
.. _FileSystemStorage (Paramteres section): http://siilo.readthedocs.org/storages/filesystem.html
