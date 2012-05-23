# python-quirc

Python ctypes interface for QR code decoding library [libquirc](https://github.com/dlbeer/quirc)

# Tests

Run tests with a `python setup.py test` command or look for [Travis build logs](http://travis-ci.org/#!/svartalf/python-quirc).

[![Build Status](https://secure.travis-ci.org/svartalf/python-quirc.png)](http://travis-ci.org/svartalf/python-quirc)

# Usage

## Low-level API

Low-level API directly corresponds to the C API:

Create new Quirc object with a `quirc.api.new` function.

    qr = quirc.api.new()

Set the image size that you'll be working with

    quirc.api.resize(qr, 640, 480)

Processing frames is done in two stages. The first stage is an image-recognition stage called identification,
which takes a grayscale image and searches for QR codes.

    buffer = quirc.api.begin(qr, 640, 480)

Now fill out this image buffer with a pixels. One byte per pixel, w pixels per line, h lines in the buffer.
Here is a simplest example from the `tests/test_quirc.py:test_fill`:

    for idx, pixel in enumerate(pixels):
        buffer[idx] = ctypes.c_uint8(ord(pixel))

After the call to `quirc.api.end`, the decoder holds a list of detected QR codes

    quirc.api.end(qr)

At this point, the second stage of processing occurs - decoding.

Number of QR codes identified in this image

    num_codes = quirc.api.count(obj)

Iterate all over the identified codes

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

    quirc.api.destroy(qr)

# Trobleshooting

If library raises an exception `OSError: libquirc.so.1: cannot open shared object file: No such file or directory`,
set environment variable LD_PRELOAD_PATH to `/usr/local/lib/` like this: `$ LD_PRELOAD_PATH=/usr/local/lib/ ./myscript.py`
