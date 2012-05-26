Streaming
=========

In case if you are detect QR codes from video stream or something else, creating all required structures for each frame
is very expensive. In that case you can operate Low-level API (*TODO: Link*) or use ``quirc.Decoder``.

Usage
-----

Create new decoder and supply to it frame' width and height: ``quirc.Decoder(640, 480)``.

For each frame call decoder method ``decode()`` and apply to it raw pixels binary data.

**Attention!** Streaming decoder suppress ``quirc.DecodeException``, because if current frame cannot be decoded,
it must not crash a program.

::

    import quirc

    # Create new decoder with frame size
    decoder = quirc.Decoder(640, 480)

    while True:

        # Use OpenCV or something else here
        # In this example, here is a pseudo-code
        image = get_new_frame_from_camera()

        # Convert it to the grayscale, so each byte will represent one pixel
        image.convert('grayscale')

        for code in decoder.raw(image.to_string()):
            print code.text

