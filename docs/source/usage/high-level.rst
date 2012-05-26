High-level API
==============

It is very simple in use::

    import quirc
    from PIL import Image

    for code in quirc.decode(Image.open('images/qr-code.png')):
        print code

.. py:function:: quirc.base.decode(raw_data)

Returns generator, which contains results of QR codes recognition.

Each item is an object with those attributes:

    corners
        Tuple with the four corners of the QR code, from top left, clockwise
    size
        The number of cells across in the QR code
    version
        QR code version
    ecc_level
        The percentage of unreadable codewords can be restored in a QR Code symbol without data loss
    data_type
        QR code type
    text
        Encoded text
