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
cv2.waitKey()
cv2.destroyAllWindows()

# 2. Split image into different channels
blue, green, red = cv2.split(img)

# Determine which channel to show
channel_input = input('> Which channel to split?(b = blue, g = green, r = red): ')

# Choose selected image
if channel_input == 'b':
    cv2.imshow('Blue Channel Splitted', blue)
elif channel_input == 'g':
    cv2.imshow('Green channel splitted', green)
elif channel_input == 'r':
    cv2.imshow('Red channel splitted', red)
else:
    print('Invalid input.')

cv2.waitKey()