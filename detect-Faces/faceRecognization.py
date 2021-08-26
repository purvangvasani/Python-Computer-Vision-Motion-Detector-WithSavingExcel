import cv2
import pandas
from datetime import datetime

# first_frame = None
# status_list = [None, None]
# times = []
# df = pandas.DataFrame(columns=['Start', 'End'])

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml")

right_eye = cv2.CascadeClassifier(
    "haarcascade_rightEye.xml")
    
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (21, 21), 0)  # to blur the image

    # if first_frame is None:
    #     first_frame = gray
    #     continue

    # delta_frame = cv2.absdiff(first_frame, gray)

    # thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # (cnts, _) = cv2.findContours(thresh_frame.copy(),
    #                              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # for contour in cnts:
    #     if cv2.contourArea(contour) < 10000:
    #         continue

    #     status = 1
    #     (x, y, w, h) = cv2.boundingRect(contour)
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
    # status_list.append(status)

    # if status_list[-1] == 1 and status_list[-2] == 0:
    #     times.append(datetime.now())
    # if status_list[-1] == 0 and status_list[-2] == 1:
    #     times.append(datetime.now())

    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.4,
                                          minNeighbors=6)

    rightEye = right_eye.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=5)

    for x, y, w, h in faces:
        gray = cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # gray = cv2.putText(gray, 'Purvang', (x, y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

    # for x, y, w, h in rightEye:
    #     gray = cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 0, 255), 3)

    cv2.imshow('Gray Frame..', gray)
    # cv2.imshow('Delta Frame..', delta_frame)
    # cv2.imshow('Threshold Frame..', thresh_frame)
    # cv2.imshow('Color Frame..', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        # if status == 1:
        #     times.append(datetime.now())
        break

# for i in range(0, len(times), 2):
#     df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

# df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
