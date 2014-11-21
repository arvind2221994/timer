from Tkinter import *
import tkMessageBox
import time
import winsound

frmMain=Tk()


def butcallback():
	#tkMessageBox.showinfo("Hello python", "Hello world")
	
	t=time.time()
	end=t+3600*int(e2.get()) + 60*int(e3.get()) + int(e4.get())
	#print add
	
	while time.time() < end:
		print str(int((end-time.time())/3600)) + ":" + str(int((end-time.time())/60)) + ":" + str(int(end-time.time()))
	
	winsound.Beep(700,7000)
	tkMessageBox.showinfo("Message", "Time's up!")
	
	
frmMain.title("Timer")
label=Label(frmMain, text="Welcome to python timer app. Enter your duration in the fields below.")	
label.pack()

label2=Label(frmMain, text="Hours:")
label2.pack()
e2= Entry(frmMain,bd=3)
e2.pack()
label3=Label(frmMain, text="Minutes:")
label3.pack()
e3= Entry(frmMain,bd=3)
e3.pack()
label4=Label(frmMain, text="Seconds:")
label4.pack()
e4= Entry(frmMain,bd=3)
e4.pack()

B = Button(frmMain,text="Start timer!", command=butcallback)
B.pack()

labelend=Label(frmMain, text="-Developed by Arvind")	
labelend.pack()
frmMain.mainloop()
