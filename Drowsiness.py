import cv2 import SmartCam
import KeyListener

Blink = 0 Create = False
cascadePath = r"xml\haarcascade_frontalface_default.xml" faceCascade = cv2.CascadeClassifier(cascadePath)
eyesCascade = cv2.CascadeClassifier("xml/haarcascade_eye_tree_eyeglasses.xml")


def Drowziness(): global Blink global Create
if Create == False:
cam = cv2.VideoCapture(0) Create = True

while SmartCam.Static == False: SmartCam.GUI.UpdateGUI(KeyListener.char_w) ret, frame = cam.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) faces = faceCascade.detectMultiScale(gray, 1.2, 7) for (x, y, w, h) in faces:
cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
roi_gray = gray[y:y + h, x:x + w] roi_color = frame[y:y + h, x:x + w]
eyes = eyesCascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=1)
for (ex, ey, ew, eh) in eyes:
cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (100, 255, 255), 2)
if len(faces) >= 1: if len(eyes) >= 2:
Blink = 0 else:
if Blink > 50: print('Sleeping') Blink = 0
else:
Blink = Blink + 1 cv2.imshow('Status', frame) cv2.waitKey(1)
if SmartCam.Static == True: SmartCam.GUI.UpdateGUI(KeyListener.char_s) Create = False
cam.release() cv2.destroyAllWindows()
