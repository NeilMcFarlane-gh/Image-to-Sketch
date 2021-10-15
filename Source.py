# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:18:52 2020

@author: Neil McFarlane
"""

import cv2 as cv2

print()
print("Please input the name of the image.")
print()

user_input = input("> ")
image = cv2.imread(user_input, 1)

alpha = 0.6
beta = 20


grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inv_gray_image = 255 - grey_image
blur_image = cv2.GaussianBlur(inv_gray_image, (21,21), 0)
inv_blur_image = 255 - blur_image
pencil_image = cv2.divide(grey_image, inv_blur_image, scale = 256.0)
contrast_pencil_image = cv2.convertScaleAbs(pencil_image, alpha=alpha, beta=beta)

cv2.imwrite("pencil.jpg", pencil_image)
cv2.imwrite("con_pencil.jpg", contrast_pencil_image)




