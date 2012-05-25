# -*- coding: utf-8 -*-

import ctypes
import time
import sys

import cv
import array
import quirc

# Create window for image showing
cv.NamedWindow('window', cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)

# Capture first frame to determine window size
frame = cv.QueryFrame(capture)
# Here it is
size = cv.GetSize(frame)

# Prepare additional object for grayscale version of the image
grayscale = cv.CreateImage(size, 8, 1)

# And the font for text drawing
font = cv.InitFont(cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 2, 2, 0, 1, 8)

# Initialize all required quirc structures
obj = quirc.api.new()
quirc.api.resize(obj, *size)

code = quirc.api.structures.Code()
data = quirc.api.structures.Data()

while True:
    # Query new frame
    frame = cv.QueryFrame(capture)

    # Make a grayscale copy
    cv.CvtColor(frame, grayscale, cv.CV_BGR2GRAY)

    # Create a buffer for recognition
    buffer = quirc.api.begin(obj, *size)

    # Fill it with a pixels data
    buf = array.array('B', grayscale.tostring())
    ctypes.memmove(buffer, buf.buffer_info()[0], size[0]*size[1])

    quirc.api.end(obj)

    for i in range(quirc.api.count(obj)):
        # Extract all QR codes
        quirc.api.extract(obj, i, code)
        try:
            quirc.api.decode(code, data)
        except quirc.DecodeException:
            continue

        # Draw a countours for each QR code
        cv.Line(frame, (code.corners[0].x, code.corners[0].y), (code.corners[1].x, code.corners[1].y), (0, 255, 0))
        cv.Line(frame, (code.corners[1].x, code.corners[1].y), (code.corners[2].x, code.corners[2].y), (0, 255, 0))
        cv.Line(frame, (code.corners[2].x, code.corners[2].y), (code.corners[3].x, code.corners[3].y), (0, 255, 0))
        cv.Line(frame, (code.corners[3].x, code.corners[3].y), (code.corners[0].x, code.corners[0].y), (0, 255, 0))

        # And a decoded text for each one
        cv.PutText(frame, ctypes.string_at(data.payload, data.payload_len), (code.corners[3].x, code.corners[3].y+14), font, (0, 0, 255))

    # Show this image in the window
    cv.ShowImage('window', frame)

    # Wait for key pressing
    key = cv.WaitKey(5)
    if key > 0:
        # And if there any key, do not forgeting to clean up memory!
        quirc.api.destroy(obj)

        # Cya!
        sys.exit()
