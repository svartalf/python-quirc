# -*- coding: utf-8 -*-

__all__ = ('ECC_LEVEL_M', 'ECC_LEVEL_L', 'ECC_LEVEL_H', 'ECC_LEVEL_Q')

# QR-code ECC types
ECC_LEVEL_M = 0
ECC_LEVEL_L = 1
ECC_LEVEL_H = 2
ECC_LEVEL_Q = 3

# QR-code data types
DATA_TYPE_NUMERIC = 1
DATA_TYPE_ALPHA = 2
DATA_TYPE_BYTE = 4
DATA_TYPE_KANJI = 8

# Limit on the maximum size of QR-code
MAX_BITMAP = 3917

# Limit on the maximum size of the QR-code content
MAX_PAYLOAD = 8896

# Various decoder errors which may occur.
# Same as a `quirc_decode_error_t` enum.
_DECODE_ERRORS = {
    1: 'Invalid grid size',
    2: 'Invalid version',
    3: 'Format data ECC failure',
    4: 'ECC failure',
    5: 'Unknown data type',
    6: 'Data overflow',
    7: 'Data underflow',
}
