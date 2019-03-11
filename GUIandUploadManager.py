import threading import tkinter as tk import KeyListener import SpeedUploader


class window(threading.Thread): def __init__(self):
threading.Thread.__init__(self,target=self.loop) self.start()

def callback(self): self.root.quit()

def UpdateGUI(self,key):
if key == KeyListener.char_u: KeyListener.Speed = 0 SpeedUploader.uploader() self.line1.config(text = '+ to add User')
self.line3.config(text = '- to remove User')
if key == KeyListener.char_plus and KeyListener.prev_key == KeyListener.char_u:
self.line1.config(text = '') self.line3.config(text = '') self.line2.config(text = 'User Added')

if key == KeyListener.char_minus and KeyListener.prev_key == KeyListener.char_u:
self.line1.config(text='') self.line3.config(text='')
self.line2.config(text = str(KeyListener.Curr_Id) + ' User Removed')q if key == KeyListener.char_w:
self.line1.config(text='')


self.line2.config(text=KeyListener.Speed) self.line3.config(text='')
if round(KeyListener.Speed)/4 == 0: SpeedUploader.uploader()
if key == KeyListener.char_s: self.line1.config(text='') self.line2.config(text=KeyListener.Speed) self.line3.config(text='') SpeedUploader.uploader()
if key == KeyListener.char_q: self.callback()

def loop(self): self.root = tk.Tk()
self.line1 = tk.Label(self.root,width = 55) self.line2 = tk.Label(self.root,width = 55) self.line3 = tk.Label(self.root,width = 55) self.line1.grid(row = 0,column = 0) self.line2.grid(row = 1,column = 0) self.line3.grid(row = 2,column = 0)
self.root.protocol("WM_DELETE_WINDOW", self.callback()) self.root.mainloop()

