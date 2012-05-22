# -*- coding: utf-8 -*-


class QuircException(BaseException):
    pass


class DecodeException(QuircException):

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message