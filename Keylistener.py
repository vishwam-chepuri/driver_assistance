from pynput.keyboard import Listener,KeyCode import SmartCam
import threading import time import ManageUsers

Speed = 0 IgnoreLoops = 0 Code = KeyCode()
char_e = code.from_char(‘e’) char_u = Code.from_char('u') char_plus = Code.from_char('+') char_minus = Code.from_char('-') char_w = Code.from_char('w') char_s = Code.from_char('s') char_q = Code.from_char('q') prev_key = None
action = None Serial = {1} Curr_Id = None

def UpdateRead(): global Curr_Id
file = open('Users.txt',mode = 'r') file.seek(0)
while True:
a = file.read(1) if a == '':
break if a != ',':
Serial.add(int(a)) file.close()
a = file.read(1) if a == '':
break else:
Curr_Id = int(a)

file.close()

def UpdateWrite(): global Serial global Curr_Id
file = open('Users.txt',mode = 'a') file2= open('curr.txt',mode='w') for a in Serial:
file.write(',') file.write(str(a))
file.close() file2.write(str(Curr_Id)) file2.close()

def press(key): global IgnoreLoops global Speed
while key == char_w: SmartCam.Static = False SmartCam.GUI.UpdateGUI(key) if Speed<10:
Speed = Speed + 0.1 if Speed >= 10:
Speed = Speed + (0.003*Speed) if Speed >=180:
key = None

def release(key): global action global Speed global Curr_Id global prev_keyu if key == char_u:
SmartCam.action = key prev_key = key
if key == char_plus and prev_key == char_u: UpdateRead() ManageUsers.addUser(Curr_Id) Serial.add(Curr_Id)
Curr_Id = Curr_Id + 1 UpdateWrite()
if key == char_e: SmartCam.Create = true
if key == char_minus and prev_key == char_u: UpdateRead()
a = input('Enter User Id') Curr_Id = int(a)
if Curr_Id in Serial: ManageUsers.removeUser(Curr_Id)
else: pass
if key == char_q: SmartCam.GUI.UpdateGUI(key) SmartCam.Access = False SmartCam.came = False SmartCam.Static = True SmartCam.GUION = False

if key == char_s: Speed = 0
SmartCam.Static = True

def handler():

with Listener(on_press=press,on_release=release) as listen: listen.join()

def runListenThread():
thread = threading.Thread(target = handler) thread.start() file = open('curr.txt',mode= 'r') file.seek(0)
while True:

