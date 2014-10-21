===============================
Flask-Storage
===============================

.. image:: https://badge.fury.io/py/flask_storage.png
    :target: http://badge.fury.io/py/flask_storage

.. image:: https://travis-ci.org/s-m-i-t-a/flask_storage.png?branch=master
        :target: https://travis-ci.org/s-m-i-t-a/flask_storage

.. image:: https://pypip.in/d/flask_storage/badge.png
        :target: https://pypi.python.org/pypi/flask_storage

.. image:: https://coveralls.io/repos/s-m-i-t-a/flask_storage/badge.png
        :target: https://coveralls.io/r/s-m-i-t-a/flask_storage


A simple storage for Flask.

* Free software: BSD license

Quickstart
----------
Install flask_storage::

    pip install flask_storage

In the app you must init the ``Storage``::

    from flask import Flask
    from flask.ext.storage import Storage

    app = Flask(__name__)
    Storage(app)
