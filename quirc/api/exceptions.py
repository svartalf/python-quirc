# -*- coding: utf-8 -*-


class QuircException(BaseException):
    # TODO: docstring
    pass


class DecodeException(QuircException, ValueError):
    # TODO: docstring

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message
