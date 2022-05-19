import socket
import time
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HOSTNAME = socket.gethostname()
connect = True
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    client.send(send_length)
    client.send(message)
def print_recieve ():
    return_message = client.recv(2048).decode(FORMAT)
    print("Server Say:" + return_message)
    return return_message
while connect:
    message = input("What do you wanna say: ")
    send(message)
    msg = print_recieve()
    if message == DISCONNECT_MESSAGE:
        connect = False
        print("Server Disconnected")     
