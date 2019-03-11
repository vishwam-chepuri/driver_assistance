import cv2 import os
import numpy as np


face_detector = cv2.CascadeClassifier('G:\python\Driver Assistance\xml\haarcascade_frontalface_default.xml')

useful = ['addUser', 'removeUser']

def getImagesAndLabels(path):
imagePaths = [os.path.join(path, f) for f in os.listdir(path)] faceSamples=[]
ids = []
for imagePath in imagePaths:
PIL_img = cv2.imread(imagePath, 0)
id = int(os.path.split(imagePath)[-1].split(".")[1]) faces = face_detector.detectMultiScale(PIL_img)

for (x, y, w, h) in faces: faceSamples.append(PIL_img[y:y+h, x:x+w]) ids.append(id)
return faceSamples, ids

def createXML():
recognizer = cv2.face.LBPHFaceRecognizer_create()
faces, ids = getImagesAndLabels('G:\python\Driver Assistance\dataset') recognizer.train(faces, np.array(ids)) recognizer.save('G:\python\Driver Assistance\ xml\Authorized.xml')

def addUser(Serial):
cap = cv2.VideoCapture(0)
#face_detector = cv2.CascadeClassifier('G:\python\Driver Assistance\ xml\haarcascade_frontalface_default.xml')

count = 0


while (True):
_, image_frame = cap.read()
gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY) faces = face_detector.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 2) count += 1
cv2.imwrite(r"G:\python\Driver Assistance\dataset\User." + str(Serial) + '.' + str(count) + ".png", gray[y:y + h, x:x + w])

cv2.imshow('addUser', image_frame)
if cv2.waitKey(10) & 0xFF == ord('q'): break
elif count >= 200: break
cap.release() cv2.destroyAllWindows()

createXML()

def removeUser(serial): try:
    for count in range(1,201):
os.remove(r"E:\Developer IDE's\PyCharm\Workspace\Driver Assistance\dataset\User." + str(serial) + '.' + str(count) + ".png")
except FileNotFoundError: print('Slot is Empty')
createXML()
