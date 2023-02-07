"""
    This file contains the utility functions for the aim of this project
"""
import cv2
from matplotlib import pyplot as plt


def get_mouth(img, face_cascade_path='cascade_files/haarcascade_frontalface_default.xml',
              mouth_cascade_path='cascade_files/haarcascade_mcs_mouth.xml'):
    """
    :img cv2 image
    @returns: json coords of rectangle containing the face and the mouth {face: ..., mouth: ...,}
    """
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    mouth_cascade = cv2.CascadeClassifier(mouth_cascade_path)

    if mouth_cascade.empty():
        raise IOError('Unable to load the mouth cascade classifier xml file')

    #img_path = "MIRACL-VC1/F01/words/01/01/color_001.jpg"
    #img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # plt.imshow(gray, cmap='gray')

    # Detect face
    face_rects = face_cascade.detectMultiScale(gray, 1.1, 3)

    for (x, y, w, h) in face_rects:
        roi_gray = gray[y:y + h, x:x + w]
        # plt.imshow(roi_gray, cmap='gray')
        mouth_rects = mouth_cascade.detectMultiScale(roi_gray, 1.4, 9)
        #cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 0, 255), 2)
        for (mx, my, mw, mh) in mouth_rects:
            my = int(my - 0.25 * mh)
            roi_gray_mouth = gray[my:my + mh, mx:mx + mw]
            #cv2.rectangle(gray, (x + mx, y + my), (x + mx + mw, y + my + mw), (255, 0, 0), 2)
            plt.imshow(roi_gray, cmap='gray')

            return roi_gray, roi_gray_mouth