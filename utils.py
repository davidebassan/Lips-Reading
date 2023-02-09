"""
    This file contains the utility functions for the aim of this project
"""
import cv2
from matplotlib import pyplot as plt


def get_mouth_old(img_path, face_cascade_path='cascade_files/haarcascade_frontalface_default.xml',
              mouth_cascade_path='cascade_files/haarcascade_mcs_mouth.xml'):

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    mouth_cascade = cv2.CascadeClassifier(mouth_cascade_path)

    if mouth_cascade.empty():
        raise IOError('Unable to load the mouth cascade classifier xml file')

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.imshow(gray, cmap='gray')

    # Detect face
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        roi_color = img[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w]
        lips = mouth_cascade.detectMultiScale(roi_gray, 1.4, 4)

        for (lx, ly, lw, lh) in lips:
            # my = int(ly - 0.25 * lh)
            lip_cropped = roi_color[ly:ly + lh, lx:lx + lw]
            # cv2.rectangle(gray, (x + mx, y + my), (x + mx + mw, y + my + mw), (255, 0, 0), 2)
            return lip_cropped


def get_mouth(img_path):
    import cv2
    import dlib
    import numpy as np

    # Carica il modello di rilevamento facciale
    face_detector = dlib.get_frontal_face_detector()

    # Carica il modello di predizione delle coordinate delle labbra
    p = "cascade_files/shape_predictor_68_face_landmarks.dat"
    lip_predictor = dlib.shape_predictor(p)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Converti l'immagine in scala di grigi
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Rileva le facce nell'immagine
    faces = face_detector(gray)

    # Loop sulle facce rilevate
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        rect = dlib.rectangle(x, y, x + w, y + h)

        # Trova le coordinate delle labbra
        shape = lip_predictor(gray, rect)
        lip_points = []
        for i in range(48, 61):
            lip_points.append([shape.part(i).x, shape.part(i).y])

        # Trova i valori massimi e minimi per x e y
        x_min = int(min([p[0] for p in lip_points]))
        x_max = int(max([p[0] for p in lip_points]))
        y_min = int(min([p[1] for p in lip_points]))
        y_max = int(max([p[1] for p in lip_points]))

        # Ritaglia la bocca
        lip_cropped = img[y_min:y_max, x_min:x_max]
        return lip_cropped