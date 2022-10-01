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

""" Function to wait for key and destroy image after
"""
def wait_and_destroy():
    cv2.waitKey()
    cv2.destroyAllWindows()

# imports
import cv2
import numpy as np

# Retrieve image
img = cv2.imread('image.jpg')
cv2.imshow('Original', img)

""" 1. Resize Image
"""
resizedImg = cv2.resize(img, (500, 500), interpolation = cv2.INTER_AREA)
cv2.imshow('Resized', resizedImg)
wait_and_destroy()

""" 2. Split image into bgr channels
"""
# Split channel
blue, green, red = cv2.split(img)

# Keep asking user input until user quits
channel_input = 0
while channel_input != 'q':
    channel_input = input('=== Which channel to split? ===\n(b = blue, g = green, r = red, q = quit)\n> ')

    # Choose selected image
    if channel_input == 'b':
        cv2.imshow('Blue Channel Splitted', blue)
        wait_and_destroy()
    elif channel_input == 'g':
        cv2.imshow('Green channel splitted', green)
        wait_and_destroy()
    elif channel_input == 'r':
        cv2.imshow('Red channel splitted', red)
        wait_and_destroy()
    elif channel_input == 'q':
        print('Quit.')
        break
    else:
        print('Invalid input.')
        break

""" 3. Convert image into pixel art
"""
# Retrieve image dimension
height, width = img.shape[0:2]

# Resize image to a small size
smallImg = cv2.resize(img, (int(width/10), int(height/10)), interpolation = cv2.INTER_LINEAR)

# Resize image back to the original size
pixelImg = cv2.resize(smallImg, (width, height), interpolation = cv2.INTER_LINEAR)
cv2.imshow('Pixel Art Image', pixelImg)
wait_and_destroy()

""" 4. Replace rising sun with face
    Code Reference: https://learnopencv.com/seamless-cloning-using-opencv-python-cpp/
"""
# Retrieve images
face_img  = cv2.imread('person_face.jpg')
face_img = cv2.resize(face_img, (200,200), interpolation = cv2.INTER_AREA)
sun_img = cv2.imread('rising_sun.jpg')

# Create mask around the face
face_mask = np.zeros(face_img.shape, face_img.dtype)
poly = np.array([ [50,0], [150,0], [150,200], [50,200] ],
                 np.int32)
cv2.fillPoly(face_mask, [poly], (255,255,255))

# Perform seamless clone
center = (500, 370)
replace_img = cv2.seamlessClone(face_img, sun_img, face_mask, 
                                center, cv2.NORMAL_CLONE)

cv2.imshow('Replaced Image', replace_img)
wait_and_destroy()


""" 5. Pick out color orange in image
    Code Reference: https://www.projectpro.io/recipes/detect-specific-colors-from-image-opencv
                    https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv
"""
# Define upper&lower limit for color 'orange'
orange_img = cv2.imread('orange.jpg')
orange_img = cv2.cvtColor(orange_img, cv2.COLOR_BGR2HSV)
lower_orange = np.array([10, 50, 70])
upper_orange = np.array([24, 255, 255])

# Detect orange color in image
color_mask = cv2.inRange(orange_img, lower_orange, upper_orange)
detect_img = cv2.bitwise_and(orange_img, orange_img, mask = color_mask)
cv2.imshow('Detected Orange', detect_img)
wait_and_destroy()
