import cv2
import GUIandUploadManager import Drowziness
import time

Static = True Access = False GUION = False GUI = None action = None Sleep = False
recognizer = cv2.face.LBPHFaceRecognizer_create() recognizer.read('xml\Authorized.xml')
cascadePath = r"xml\haarcascade_frontalface_default.xml" faceCascade = cv2.CascadeClassifier(cascadePath)
eyesCascade = cv2.CascadeClassifier("xml/haarcascade_eye_tree_eyeglasses.xml") font = cv2.FONT_HERSHEY_SIMPLEX
cam = None Create = False came = False def SmartCam():
global Sleep global Access global GUION
global GUI, cam, Create, came if Create == true:
cam = cv2.VideoCapture(0) Create = False
came = True

if Access == True:
if GUION == False:
GUI = GUIandUploadManager.window() GUION = True
GUI.UpdateGUI(action)

if Static == True and Access == False: ret, frame = cam.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) faces = faceCascade.detectMultiScale(gray, 1.2, 7) cv2.imshow('Status', frame)
cv2.waitKey(1)
for (x, y, w, h) in faces:
cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 2)
Id, confidence = recognizer.predict(gray[y:y + h, x:x + w]) if (confidence < 50):
if Id:
Id = "Authorized {0:.2f}%".format(round(100 - confidence, 2)) cam.release()
cv2.destroyAllWindows() Access = True
cv2.rectangle(frame, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
cv2.putText(frame, str(Id), (x, y - 40), font, 1, (255, 255, 255), 3) if Static == False and Access == True:
Drowziness.Drowziness()
