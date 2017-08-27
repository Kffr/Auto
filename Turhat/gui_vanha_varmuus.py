import os
import sys
from Tkinter import * 
import Tkinter as tk
import webbrowser
chrome_path = '/usr/bin/google-chrome %s'


	

class App:
  def __init__(self, master):
	self.master=master
	pad=1
	master.geometry("{0}x{1}+0+0".format(
		master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
	frame = tk.Frame(master)
	frame.pack()
	frame.focus_set()
	frame.pack(anchor='sw')
	
	def Selain():
		webbrowser.open('http://www.iltalehti.fi')
     
	def Mittaristo():
		try:
			os.system('pkill -f obd_gui.py')
			os.system('sudo python obd_gui.py &')
		except:
			pass
	def Bluetooth():
		os.system('sudo /etc/init.d/bluetooth restart')
		os.system('sudo hidd --connect aa:bb:cc:dd:ee:ff')
	def Wifi():
		pass
	
	self.button1 = Button(frame, width="20", height="10", text="Selain", highlightthickness="5", highlightcolor="blue", bg="lightblue", activebackground="lightblue", command=Selain)
	self.button1.focus_set()
	self.button1.pack(side=LEFT)
	self.button2 = Button(frame, width="20", height="10", text="Mittaristo", highlightthickness="5", highlightcolor="blue", bg="lightblue", activebackground="lightblue", command=Mittaristo)
	self.button2.pack(side=LEFT)
	self.button3 = Button(frame, width="20", height="10", text="WiFi", highlightthickness="5", highlightcolor="blue", bg="lightblue", activebackground="lightblue", command=Wifi)
	self.button3.pack(side=LEFT)	
	self.button4 = Button(frame, width="20", height="10", text="Bluetooth", highlightthickness="5", highlightcolor="blue", bg="lightblue", activebackground="lightblue", command=Bluetooth)
	self.button4.pack(side=LEFT)
		
	

	def leftKey(event):
		
		if root.focus_get() == self.button1:
			self.button4.focus_set()
			self.button4.pack()
			
		elif root.focus_get() == self.button2:
			self.button1.focus_set()
			self.button1.pack()
		
		elif root.focus_get() == self.button3:
			self.button2.focus_set()
			self.button2.pack()
			
		elif root.focus_get() == self.button4:
			self.button3.focus_set()
			self.button3.pack()
			
	def rightKey(event):
		
		if root.focus_get() == self.button1:
			self.button2.focus_set()
			self.button2.pack()
		elif root.focus_get() == self.button2:
			self.button3.focus_set()
			self.button3.pack()
		elif root.focus_get() == self.button3:
			self.button4.focus_set()
			self.button4.pack()
		elif root.focus_get() == self.button4:
			self.button1.focus_set()
			self.button1.pack()
			
	def returnKey(event):
		target = root.focus_get()
		if target == self.button1:
			Selain()
		elif target == self.button2:
			Mittaristo()
		elif target == self.button3:
			Wifi()
		elif target == self.button4:
			Bluetooth()
			
	def Escape(event):
		os.system('pkill -f obd_gui.py')
		
	root.bind('<Return>', returnKey)		
	root.bind('<Right>', rightKey)	
	root.bind('<Left>', leftKey)
	root.bind('<Escape>', Escape)
	frame.pack()
root = Tk()
root.title("Kotiruutu")
root.config(bg="gray")
app = App(root)
root.mainloop()
