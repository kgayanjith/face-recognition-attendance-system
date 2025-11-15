import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
from PIL import Image

video_capture = cv2.VideoCapture(0)

rayans_image = face_recognition.load_image_file("photos/rayan.jpg")
rayans_encoding = face_recognition.face_encodings(rayans_image)[0]

kevins_image = face_recognition.load_image_file("photos/kevin.jpeg")
kevins_encoding = face_recognition.face_encodings(kevins_image)[0]

shaggys_image = face_recognition.load_image_file("photos/shaggy.jpg")
shaggys_encoding = face_recognition.face_encodings(shaggys_image)[0]

presidents_image = face_recognition.load_image_file("photos/president.jpg")
presidents_encoding = face_recognition.face_encodings(presidents_image)[0]

know_face_encoding = [
    rayans_encoding,
    kevins_encoding,
    shaggys_encoding,
    presidents_encoding
]

know_faces_names = [
    "rayan",
    "kevin",
    "shaggy",
    "president"
]

students = know_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv' , 'w+', newline = '')
lnwriter = csv.writer(f)