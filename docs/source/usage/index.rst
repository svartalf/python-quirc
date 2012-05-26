Usage
=====

Library' usage splits into a two parts: *high-level* and *low-level* API.

In a sunny and beautiful world you will need only a *high-level* API.

For decoding images from the video streaming in the realtime use Streaming decoder (`TODO: link`).

But if you are have not so much free memory or want to control whole the process, use a *low-level* API.

.. toctree::
    :maxdepth: 1

    high-level
    streaming
    low-level

Data format
-----------

All functions of the library receives image data in a binary format. There is some rules that must be applied to your data:

* Data length must be equal to the ``width`` * ``height`` of the image.
* Each byte **must** represent one pixel, so you will need manually to convert it to the *grayscale* or *black&white* mode.
