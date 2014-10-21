===============================
Flask-Storage
===============================

.. image:: https://badge.fury.io/py/flask_siilo.png
    :target: http://badge.fury.io/py/flask_siilo

.. image:: https://travis-ci.org/s-m-i-t-a/flask_siilo.png?branch=master
        :target: https://travis-ci.org/s-m-i-t-a/flask_siilo

.. image:: https://pypip.in/d/flask_siilo/badge.png
        :target: https://pypi.python.org/pypi/flask_siilo

.. image:: https://coveralls.io/repos/s-m-i-t-a/flask_siilo/badge.png
        :target: https://coveralls.io/r/s-m-i-t-a/flask_siilo


A simple storage for Flask.

* Free software: BSD license

Quickstart
----------
Install flask_siilo::

    pip install flask_siilo

In the app you must init the ``Storage``::

    from flask import Flask
    from flask.ext.siilo import Storage

    app = Flask(__name__)
    Storage(app)
