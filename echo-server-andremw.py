import socket
from termcolor import colored
import time
import re

# for the Python-side passing of commands
#HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = socket.gethostname() # or just use (host == '')
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Flags for different modes of operation
talkToCommsClient = True
listenToCommsClient = True
talkToArduino = False
listenToArduino = False

stringFromClient = ''

def help_info():
    print(colored('Client asked for help', 'magenta'))
    
def arduino_info():
    print(colored('Client asked for list of Arduino NodeId values', 'magenta')) 

def client_quit():
    print(colored('Client asked to quit connection', 'red')) 

def client_stop():
    print(colored('Client asked to stop server', 'red')) 

# Interpreter for user string input from client
def read_string_interpreter(readString,talkToCommsClient,talkToArduino,listenToCommsClient):
    if re.search("help", readString, re.IGNORECASE):
        help_info()
    if re.search("arduino", readString, re.IGNORECASE):
        arduino_info()
    if re.search("stop", readString, re.IGNORECASE):
        client_stop()
        talkToCommsClient = False   # close comms with server
        listenToCommsClient = False
    if re.search("quit", readString, re.IGNORECASE):
        client_quit()
        talkToCommsClient = False   # close comms with server
    return talkToCommsClient,talkToArduino,listenToCommsClient

# Listening to Comms Client
while listenToCommsClient:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            currentTime = time.ctime(time.time())#  + "\r\n"
            print(currentTime)
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                dataString = data.decode()
                talkToCommsClient,talkToArduino,listenToCommsClient = read_string_interpreter(dataString,talkToCommsClient,talkToArduino,listenToCommsClient)
                if data:
                    stringFromClient = dataString
                #print(colored('Remote client says: ','cyan') + dataString)  # THIS LINE KILLS IT
                if not data:
                    break
                conn.sendall(data)
            #print(colored('Remote client says: ','cyan') + stringFromClient)  # THIS LINE KILLS IT