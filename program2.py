import socket
import time
import threading
from tkinter import *

#main Window 
root = Tk()
root.geometry("300x500")
root.config(bg="White")

def func():
    t = threading.Thread(target=recv)
    t.start()

#recieved function    
def recv():
    listensocket = socket.socket()
    port = 4050
    maxconnection = 99
    ip = socket.gethostname()

    listensocket.bind(('', port))
    listensocket.listen(maxconnection)
    (clientsocket, address) = listensocket.accept()

    try:
        while True:
            sendermessage = clientsocket.recv(1024).decode()
            if not sendermessage == "":
                time.sleep(5)
                listbx.insert(0, "Client : " + sendermessage)
    except ConnectionResetError:
        print("Connection closed by the client.")
    finally:
        listensocket.close()
            

#send function         
xr = 0
def sendmsg():
    global s
    global xr
    if xr==0:
        s=socket.socket()
        hostname="192.168.8.101" #this need to change in second computer
        port=5000 #use same port in receving part in second computer
        s.connect((hostname,port))
        msg=messageboxentry.get()
        listbx.insert(0,"You : "+msg) 
        s.send(msg.encode())
        xr=xr+1
    else:
        msg=messageboxentry.get()
        listbx.insert(0,"You : "+msg)
        s.send(msg.encode())

def threadsendmsg():
    th = threading.Thread(target=sendmsg)
    th.start()
    
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