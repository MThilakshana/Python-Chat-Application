import socket
import time
import threading
from tkinter import *

#main Window 
root = Tk()
root.geometry("300x500")
root.config(bg="White")

def func():
    pass

def threadsendmsg():
    pass

startchatimage = PhotoImage(file='C:/Users/DELL/Desktop/Python/Chat appliction/button.png')

buttons = Button(root,image=startchatimage,
                 bg="white",
                 borderwidth=0,
                 cursor="hand2",
                 command=func)
buttons.place(x=60,y=10)

message = StringVar()
messageboxentry = Entry(root,
                   textvariable=message,
                   font=('calibre',10),
                   border=2,
                   width=32)
messageboxentry.place(x=10,y=444)

sendmessageimg = PhotoImage(file='C:/Users/DELL/Desktop/Python/Chat appliction/send.png')

sendbutton = Button(root,
                    image=sendmessageimg,
                    borderwidth=0,
                    bg="white",
                    cursor="hand2",
                    command=threadsendmsg)
sendbutton.place(x=255,y=437)

listbx = Listbox(root,
                 height=20,
                 width=43,
                 border=2)
listbx.place(x=15,y=80)

root.mainloop()