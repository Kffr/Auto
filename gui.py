import os, pwd
import sys
from Tkinter import * 
#import Tkinter as tk
import webbrowser
import subprocess
from subprocess import call



	

class App:
  def __init__(self, master):
	self.master=master
	pad=1
	master.geometry("{0}x{1}+0+0".format(
		master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
	#frame = tk.Frame(master)
	#frame.pack()
	#frame.focus_set()
	#frame.pack(anchor='sw')
	#frame2 = tk.Frame(master)
	#frame2.pack(side=LEFT)
	
	def Valitsin():
		
		def VaihtoV(event):
			if root.focus_get() == self.Radio1:
				self.RPeruuta.focus_set()
			elif root.focus_get() == self.Radio2:
				self.Radio1.focus_set()
			elif root.focus_get() == self.RPeruuta:
				self.Radio3.focus_set()
			elif root.focus_get() == self.Radio3:
				self.Radio2.focus_set()
			
		def VaihtoO(event):
			
			if root.focus_get() == self.Radio1:
				self.Radio2.focus_set()
			elif root.focus_get() == self.Radio2:
				self.Radio3.focus_set()
			elif root.focus_get() == self.Radio3:
				self.RPeruuta.focus_set()
			elif root.focus_get() == self.RPeruuta:
				self.Radio1.focus_set()
				
		def VaihtoValitse(event):
			
			if root.focus_get() == self.Radio1:
				Radiorock()
			elif root.focus_get() == self.Radio2:
				RadioSuom()
			elif root.focus_get() == self.Radio3:
				RadioSuomP()
			elif root.focus_get() == self.RPeruuta:
				RadioPois()
				 
				
		
		def Vbindit():
			root.bind('<Return>', VaihtoValitse)		
			root.bind('<Left>', VaihtoV)
			root.bind('<Right>',VaihtoO)
		try:
			FFauki = subprocess.check_output('pidof mplayer', shell=True)
			os.system('sudo kill -s TERM $(pidof mplayer)')
			Bindit()
		except:
			Vbindit()
			self.Radio1 = Button(root, width="10", highlightthickness="5", highlightcolor="blue", bg="lightblue", text="RadioRock", command=Radiorock)
			self.Radio1.grid(row=2, column=0, columnspan=3, pady=10, sticky=N+W)
			self.Radio2 = Button(root, width="10", highlightthickness="5", highlightcolor="blue", bg="lightblue", text="Radio SuomiRock", command=RadioSuom)
			self.Radio2.grid(row=2, column=1, columnspan=3, pady=10, sticky=N+W)
			self.Radio3 = Button(root, width="10", highlightthickness="5", highlightcolor="blue", bg="lightblue", text="Radio SuomiPop", command=RadioSuomP)
			self.Radio3.grid(row=2, column=2, columnspan=3, pady=10, sticky=N+W)
			self.Radio1.focus_set()
			self.RPeruuta = Button(root, width="10", highlightthickness="5", highlightcolor="blue", bg="lightblue", text="Peruuta", command=RadioPois)
			self.RPeruuta.grid(row=2, column=3, columnspan=3, pady=10, sticky=N+W)
			
	def RadioPois():
		self.Radio2.destroy()
		self.Radio1.destroy()
		self.Radio3.destroy()
		self.RPeruuta.destroy()
		self.button1.focus_set()
		Bindit()
			
	def RadioSuom():
		Bindit()
		self.Radio2.destroy()
		self.Radio1.destroy()
		self.Radio3.destroy()
		self.RPeruuta.destroy()
		self.button1.focus_set()
		os.system('mplayer http://stream2.bauermedia.fi/suomirock.mp3 &')
	def RadioSuomP():
		Bindit()
		self.Radio2.destroy()
		self.Radio1.destroy()
		self.Radio3.destroy()
		self.RPeruuta.destroy()
		self.button1.focus_set()
		
		os.system('mplayer http://icelive0.80692-icelive0.cdn.qbrick.com/10566/80692_RadioSuomipop.mp3 &')
			
	def Radiorock():
		Bindit()
		self.Radio2.destroy()
		self.Radio1.destroy()
		self.Radio3.destroy()
		self.RPeruuta.destroy()
		self.button1.focus_set()
		os.system('mplayer http://icelive0.80692-icelive0.cdn.qbrick.com/10565/80692_RadioRock.mp3 &')
						
	def Mittaristo():
		try:
			os.system('sudo pkill -f obd_gui.py')
			os.system('cd /home/pi/pyobd-pi && sudo ./obd_gui.py')
		except:
			pass
	def Bluetooth():
		os.system('pulseaudio --start &')
		os.system('pulseaudio -D & wait')
		os.system('~/pyobd-pi/./yhdista &')
		
		try:
			bt = subprocess.check_output("sudo /etc/init.d/bluetooth status | grep Quitting", shell=True)
			bttext = "Bluetooth: OFF"
			self.bt1.config(text=bttext, bg="red")
			
		except:
			#os.system('sudo service bluetooth start')
			bt = subprocess.check_output("sudo /etc/init.d/bluetooth status | grep Running", shell=True)
			bttext = "Bluetooth: ON"
			self.bt1.config(text=bttext, bg="green")
		
		checkbt = subprocess.check_output("pacmd list-sinks | grep device.description", shell=True).lstrip()
		self.btcheck.configure(text=checkbt)
		
				
								
	def Spotify():
		os.system('sudo pkill -f ncmpcpp')
		os.system('lxterminal --geometry=150x50 -e ncmpcpp -s playlist-editor &')

		

	
	self.button1 = Button(root, width="10", height="5", text="Radiot", highlightthickness="5", highlightcolor="blue", bg="green", activebackground="green", command=Valitsin)
	self.button1.focus_set()
	self.button1.grid(row=0, column=0, sticky=W+N, pady=(10,50))
	#self.button1.pack(side=LEFT)
	self.button2 = Button(root, width="10", height="5", text="Mittaristo", highlightthickness="5", highlightcolor="blue", bg="green", activebackground="green", command=Mittaristo)
	self.button2.grid(row=0, column=1, sticky=W+N, pady=(10,50))
	#self.button2.pack(side=LEFT)
	self.button3 = Button(root, width="10", height="5", text="Spotify", highlightthickness="5", highlightcolor="blue", bg="green", activebackground="green", command=Spotify)
	self.button3.grid(row=0, column=2, sticky=W+N, pady=(10,50))
	#self.button3.pack(side=LEFT)	
	self.button4 = Button(root, width="10", height="5", text="Bluetooth", highlightthickness="5", highlightcolor="blue", bg="green", activebackground="green", command=Bluetooth)
	self.button4.grid(row=0, column=3, sticky=W+N, pady=(10,50))
	
	
	
	#self.button4.pack(side=LEFT)
	bttext = ""
	wttext =""
	self.bt1 = Label(root, width=30, anchor=W, text=bttext)
	self.bt1.grid(row=6, column=0, columnspan=3, sticky=W)
	
	#self.bt1.pack(fill=Y)
	self.wt1 = Label(root, width=30, anchor=W, text=wttext, background="green")
	self.wt1.grid(row=4, column=0, columnspan=3, sticky=W)
	#self.wt1.pack(fill=Y)
	try:
		bt = subprocess.check_output("sudo /etc/init.d/bluetooth status | grep Running", shell=True)
		bttext = "Bluetooth: ON"
		self.bt1.config(text=bttext, bg="green")
			
	except:
		
		bt = subprocess.check_output("sudo /etc/init.d/bluetooth status | grep Quitting", shell=True)
		bttext = "Bluetooth: OFF"
		self.bt1.config(text=bttext, bg="red")
	
	try:
		wt = subprocess.check_output("rfkill list 0 | grep yes", shell=True)
		wttext = "WiFi: OFF"
		self.wt1.config(text=wttext, background="red")
	except:
		wttext ="WiFi: ON"
		self.wt1.config(text=wttext, background="green")
		pass;
		
	self.ip1 = Label(root, anchor=W, text="", justify=LEFT)
	self.ip1.grid(row=5, column=0, columnspan=4, sticky=W, pady=(0,10))
	
	self.btcheck = Label(root, anchor=W, text="", justify=LEFT, background="green")
	self.btcheck.grid(row=7, column=0, columnspan=4, sticky=W, pady=(0,10))
	def HaeTiedot():
		
		try:	
			checkbt = subprocess.check_output("pacmd list-sinks | grep device.description", shell=True).lstrip()
			self.btcheck.configure(text=checkbt)
		except:
			checkbt=" "	
		try:
			ip = subprocess.check_output("ifconfig | grep 'inet addr:19'", shell=True).strip(" ")
			self.ip1.config(bg="green", text=ip)
 		except:
			
			ip = "No connection"
			self.ip1.config(bg="red", text=ip)
			
		root.after(10000, HaeTiedot)
			
	def leftKey(event):
		
		if root.focus_get() == self.button1:
			self.button4.focus_set()
			#self.button4.pack()
			
		elif root.focus_get() == self.button2:
			self.button1.focus_set()
			#self.button1.pack()
		
		elif root.focus_get() == self.button3:
			self.button2.focus_set()
			#self.button2.pack()
			
		elif root.focus_get() == self.button4:
			self.button3.focus_set()
			#self.button3.pack()
			
	def rightKey(event):
		
		if root.focus_get() == self.button1:
			self.button2.focus_set()
			#self.button2.pack()
		elif root.focus_get() == self.button2:
			self.button3.focus_set()
			#self.button3.pack()
		elif root.focus_get() == self.button3:
			self.button4.focus_set()
			#self.button4.pack()
		elif root.focus_get() == self.button4:
			self.button1.focus_set()
			#self.button1.pack()
			
	def returnKey(event):
		target = root.focus_get()
		if target == self.button1:
			Valitsin()
		elif target == self.button2:
			Mittaristo()
		elif target == self.button3:
			Spotify()
		elif target == self.button4:
			Bluetooth()
			
	def Escape(event):
		os.system('pkill -f obd_gui.py')
		
	def Bindit():
		root.bind('<Return>', returnKey)		
		root.bind('<Right>', rightKey)	
		root.bind('<Left>', leftKey)
		root.bind('<Escape>', Escape)
	
	#frame.pack()
	Bindit()
	HaeTiedot()
root = Tk()
root.title("Kotiruutu")
root.config(bg="black")
root.attributes("-fullscreen", True)
app = App(root)

root.mainloop()
