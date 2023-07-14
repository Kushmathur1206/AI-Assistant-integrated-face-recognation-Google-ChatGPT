import cv2
import numpy as np
import csv
import os
from datetime import datetime
import face_recognition

# from Fac-rec import SimpleFacerec

def fc():
    # sfr = face_recognition.SimpleFacerec
    alg = "haarcascade_frontalface_default.xml"
    haar_cascade = cv2.CascadeClassifier(alg)
    fp = r'photos'
    lf = os.listdir(fp)

    known_face_encoding = []
    known_face_names = []

    video_capture = cv2.VideoCapture(0)

    for yfn in lf:
        known_face_names.append(yfn.split('.')[0])

    for i in range(len(lf)):
        Bill_image = face_recognition.load_image_file("photos/" + lf[i])
        Bill_encoding = face_recognition.face_encodings(Bill_image)[0]
        known_face_encoding.append(Bill_encoding)

    for i in range(len(lf)):
        # print(known_face_encoding[i])
        print(known_face_names[i])

    students = known_face_names.copy()

    face_locations = []
    face_encodings = []
    face_names = []
    s = True

    # now = datetime.now()
    # current_date = now.strftime("%Y-%m-%d")
    #
    # f = open(current_date + '.csv', 'w+', newline='')
    # inwriter = csv.writer(f)
    while True:
        if s != True:
            break
        _, frame = video_capture.read()
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
        for (x, y, w, h) in face:
            text = "Face Detected"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

        if s:

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
                name = ""
                face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
                if name in known_face_names:
                    cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200))
                    if name in students:
                        students.remove(name)
                        print(name)
                        rname = name
                        s = False
                        cv2.destroyAllWindows()

            cv2.imshow("Face Recognation", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    video_capture.release()
    return rname