from socket import *
from threading import *
from tkinter import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)