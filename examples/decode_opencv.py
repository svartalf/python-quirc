# -*- coding: utf-8 -*-

import ctypes
import sys

import cv
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

# Initialize QR decoder
decoder = quirc.Decoder(*size)

while True:
    # Query new frame
    frame = cv.QueryFrame(capture)

    # Make a grayscale copy
    cv.CvtColor(frame, grayscale, cv.CV_BGR2GRAY)

    for code in decoder.decode(grayscale.tostring()):

        # Draw a countours for each QR code
        # TODO: replace with a cv.PolyLine
        cv.Line(frame, (code.corners[0][0], code.corners[0][1]), (code.corners[1][0], code.corners[1][1]), (0, 255, 0))
        cv.Line(frame, (code.corners[1][0], code.corners[1][1]), (code.corners[2][0], code.corners[2][1]), (0, 255, 0))
        cv.Line(frame, (code.corners[2][0], code.corners[2][1]), (code.corners[3][0], code.corners[3][1]), (0, 255, 0))
        cv.Line(frame, (code.corners[3][0], code.corners[3][1]), (code.corners[0][0], code.corners[0][1]), (0, 255, 0))

        # And a decoded text for each one
        cv.PutText(frame, code.text, (code.corners[3][0], code.corners[3][1]+14), font, (0, 0, 255))

    # Show this image in the window
    cv.ShowImage('window', frame)

    # Wait for key pressing
    key = cv.WaitKey(5)
    if key > 0:
        # If any key presses, exit
        sys.exit()
