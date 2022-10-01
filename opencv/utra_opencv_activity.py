""" File: UTRA OpenCV Activity
    Date: Sat Oct 1 2022
    Author: Gil Hwang
"""

""" Instruction:
    1. Take an input image and an output image size and then map that image to the output size using OpenCV (What are the different techniques of resizing?).
    2. Take an input image and split into its different channels (bonus if you can allow the user to select which color space).
    3. Take an input image and turn it into pixel art (What OpenCV functions can you use??)
    4. Take an image of the rising sun and replace the sun with either Ammar’s, Satvick’s, or any of your friend’s faces (OpenCV).
    5. Pick out the color “orange” in any input image.
"""
# import OpenCV
import cv2

# Retrive image
img = cv2.imread('image.jpg')
cv2.imshow('Original', img)

# 1. Resize image
resizedImg = cv2.resize(img, (500, 500), interpolation = cv2.INTER_AREA)
cv2.imshow('Resized', resizedImg)

# # 2. Split image into different channels
# blue, green, red = cv2.split(img)
# cv2.imshow('Blue channel', blue)
# cv2.imshow('Green channel', green)
# cv2.imshow('Red channel', red)

cv2.waitKey()