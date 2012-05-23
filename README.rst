python-quirc
============

Python ctypes interface for QR code decoding library `libquirc <https://github.com/dlbeer/quirc/>`_.

Tests
-----

Run tests with a `python setup.py test` command or look for `Travis build logs <http://travis-ci.org/#!/svartalf/python-quirc>`_.

.. image:: https://secure.travis-ci.org/svartalf/python-quirc.png

Versioning and API stability
----------------------------

API stability isn't guaranteed before ``1.0.0`` version. Versioning is propagated by `semver.org <http://semver.org>`_.

When version ``1.0.0`` will be released the API will be frozen, and any changes which aren't backwards compatible will force a major version bump.

Usage
-----

High-level API
``````````````

Just call a `quirc.decode()` function with a `PIL.Image` object as a parameter, like this:

.. code-block::

    import Image

    image = Image.open('tests/images/test1.png')
    for code in quirc.decode(image):
        print code['text']
        # >>> test1

Currently only ``PIL`` is supported.

Low-level API
`````````````

Low-level API directly corresponds to the C API:

Create new `Quirc` object with a `quirc.api.new` function.

.. code-block::

    qr = quirc.api.new()

Set the image size that you'll be working with

.. code-block::

    quirc.api.resize(qr, 640, 480)

Processing frames is done in two stages. The first stage is an image-recognition stage called identification,
which takes a grayscale image and searches for QR codes.

.. code-block::

    buffer = quirc.api.begin(qr, 640, 480)

Now fill out this image buffer with a pixels. One byte per pixel, w pixels per line, h lines in the buffer.
Here is a simplest example from the `tests/test_quirc.py:test_fill`:

.. code-block::

    for idx, pixel in enumerate(pixels):
        buffer[idx] = ctypes.c_uint8(ord(pixel))

After the call to `quirc.api.end`, the decoder holds a list of detected QR codes

.. code-block::

    quirc.api.end(qr)

At this point, the second stage of processing occurs - decoding.

Number of QR codes identified in this image

.. code-block::

    num_codes = quirc.api.count(obj)

Iterate all over the identified codes

.. code-block::

    for i in range(num_codes):
        # Prepare required structures for data filling

        # `quirc.api.structures.Code` structure contains information about detected QR code in the input image
        code = quirc.api.structures.Code()
        quirc.api.extract(qr, i, ctypes.byref(code))

        # `quirc.api.structures.Data` holds the decoded QR code data
        data = quirc.api.structures.Data()
        quirc.api.decode(ctypes.byref(code), ctypes.byref(data))

        # Extracting QR-encoded string now
        print ctypes.string_at(data.payload, data.payload_len)

Finally, release the allocated memory

.. code-block::

    quirc.api.destroy(qr)

Trobleshooting
--------------

If library raises an exception `OSError: libquirc.so.1: cannot open shared object file: No such file or directory`,
set environment variable LD_PRELOAD_PATH to `/usr/local/lib/` like this: `$ LD_PRELOAD_PATH=/usr/local/lib/ ./myscript.py`

Contributing
------------

If you want to contribute, follow the `pep8 <http://www.python.org/dev/peps/pep-0008/>`_ guideline, and include the tests.