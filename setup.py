# -*- coding: utf-8 -*-

from setuptools import setup

import quirc

setup(
    name='quirc',
    version=quirc.__version__,
    license=open('LICENSE').read(),
    author='SvartalF',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-quirc',
    description='ctypes wrapper for QR code decoding library `libquirc`',
    packages=('quirc',),
    test_suite='tests.load_tests',
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Multimedia :: Graphics',
    ),
)
