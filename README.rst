python-quirc
============

Python ctypes interface for QR code decoding library `libquirc <https://github.com/dlbeer/quirc/>`_.

Tests
-----

Run tests with a ``python setup.py test`` command or look for `Travis build logs <http://travis-ci.org/#!/svartalf/python-quirc>`_.

.. image:: https://secure.travis-ci.org/svartalf/python-quirc.png

Versioning and API stability
----------------------------

API stability isn't guaranteed before ``1.0.0`` version. Versioning is propagated by `semver.org <http://semver.org>`_.

When version ``1.0.0`` will be released the API will be frozen, and any changes which aren't backwards compatible will force a major version bump.

Documentation
-------------

Read the documentation and usage examples `here <http://python-quirc.readthedocs.org>`_.

Trobleshooting
--------------

If library raises an exception ``OSError: libquirc.so.1: cannot open shared object file: No such file or directory``,
set environment variable LD_PRELOAD to ``/usr/local/lib/libquirc.so`` like this: ``$ LD_PRELOAD=/usr/local/lib/libquirc.so ./myscript.py``

Contributing
------------

If you want to contribute, follow the `pep8 <http://www.python.org/dev/peps/pep-0008/>`_ guideline, and include the tests.