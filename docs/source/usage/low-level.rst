Low-level API
==============

Low-level API fully copies the C API and is contained in the ``quirc.api`` module.

See `example`_ for workflow.

**Warning**: you will need to use ``ctypes`` here manually.

Functions
---------

Initialization
``````````````

.. autofunction:: quirc.api.new

.. autofunction:: quirc.api.destroy

.. autofunction:: quirc.api.resize

Recognition
```````````

.. autofunction:: quirc.api.begin

.. autofunction:: quirc.api.end

Extraction
``````````

.. autofunction:: quirc.api.count

.. autofunction:: quirc.api.extract

.. autofunction:: quirc.api.decode

Miscellaneous
`````````````

.. autofunction:: quirc.api.version

Classes
-------

.. autoclass:: quirc.api.structures.Quirc

.. autoclass:: quirc.api.structures.Code

.. autoclass:: quirc.api.structures.Point

.. autoclass:: quirc.api.structures.Data

Example
-------

::

    from quirc import api
    from PIL import Image

    image = Image.open('images/qr-code.png')
    width, height = image.size

    # Convert image to the grayscale mode
    if not image.mode in ('L', '1'):
        image = image.convert('L')
    pixels = image.load()

    obj = api.new()
    api.resize(obj, width, height)

    buffer = api.begin(obj, width, height)

    # Fill buffer with a image pixels. One cell, one pixel.
    idx = 0
    for i in range(width):
        for j in range(height):
            buffer[idx] = ctypes.c_uint8(pixels[j, i])
            idx += 1

    # Finish image recognition
    api.end(obj)

    code = api.structures.Code()
    data = api.structures.Data()

    for i in range(api.count(obj)):
        api.extract(obj, i, code)
        api.decode(code, data)

        print ctypes.string_at(data.payload, data.payload_len)

    api.destroy(obj)

