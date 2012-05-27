High-level API
==============

It is very simple in use::

    import quirc
    from PIL import Image

    for code in quirc.decode(Image.open('images/qr-code.png')):
        print code

.. autofunction:: quirc.decode

.. autoclass:: quirc.base.Code
