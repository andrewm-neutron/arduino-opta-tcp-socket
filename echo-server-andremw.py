import socket
from termcolor import colored
import time
import re
from opcua import Client
import numpy as np

# for the Python-side passing of commands
#HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = socket.gethostname() # or just use (host == '')
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# for Arduino Opta PLC running OPC UA Server
url = "opc.tcp://192.168.29.180:4840"

# Flags for different modes of operation
talkToCommsClient = True
listenToCommsClient = True
talkToArduino = False
listenToArduino = False

stringFromClient = ''

def wrong_cmd():
    print(colored('Client entered an incorrect command', 'red')) 

def help_info():
    print(colored('Client asked for help', 'magenta'))
    
def arduino_info():
    print(colored('Client asked for list of Arduino NodeId values', 'magenta')) 

def client_quit():
    print(colored('Client asked to quit connection', 'red')) 

def client_stop():
    print(colored('Client asked to stop server', 'red'))
    
def unknown_cmd():
    print(colored('Client entered unknown command', 'magenta'))
    
def empty_cmd():
    print(colored('Empty string sent', 'yellow'))
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    
def client_readNode(NodeId):
    NodeIdString = str(NodeId)
    print(colored('Client asked to read NodeId ', 'yellow') + NodeIdString)
    NodeId = 'i='+NodeId
    client = Client(url)
    client.connect()
    node = client.get_node(NodeId)
    reply = node.get_value()
    #print(reply)
    client.disconnect()
    return reply
    
def client_writeNode(NodeId,value):
    NodeIdString = str(NodeId)
    ValueString = str(value)
    NodeId = 'i='+NodeId
    print(colored('Client asked to write NodeId ', 'yellow') + NodeIdString + colored(' to ', 'yellow') + ValueString)
    client = Client(url)
    client.connect()
    node = client.get_node(NodeId)
    value = bool(value)
    node.set_data_value(value)
    client.disconnect()
    #return reply
=======
>>>>>>> 13bc130713e5a3a42d1aa0090c8050b29bf9ad96
>>>>>>> Stashed changes

# Interpreter for user string input from client
def read_string_interpreter(readString,talkToCommsClient,talkToArduino,listenToCommsClient):
    knownCmd = False
    # if not readString:
    #     empty_cmd()
    if re.search("help", readString, re.IGNORECASE):
        knownCmd = True
        help_info()
    if re.search("arduino", readString, re.IGNORECASE):
        knownCmd = True
        arduino_info()
    if re.search("stop", readString, re.IGNORECASE):
        knownCmd = True
        client_stop()
        talkToCommsClient = False   # close comms with server
        listenToCommsClient = False
    if re.search("quit", readString, re.IGNORECASE):
        knownCmd = True
        client_quit()
        talkToCommsClient = False   # close comms with server
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    if re.search("readNode", readString, re.IGNORECASE):
        knownCmd = True
        cmdString = readString.split('(')
        cmdString = cmdString[1].split(')')
        cmStringTest = cmdString[0].split(',')
        if not np.size(cmStringTest) == 1:
            wrong_cmd()
        nodeToRead = cmdString[0]
        reply = client_readNode(nodeToRead)
        print(reply)
    if re.search("writeNode", readString, re.IGNORECASE):
        knownCmd = True
        cmdString = readString.split('(')
        cmdString = cmdString[1].split(')')
        cmdString = cmdString[0].split(',')
        cmStringTest = cmdString[0].split(',')
        if not np.size(cmStringTest) == 2:
            wrong_cmd()
        nodeToRead = cmdString[0]
        valueToWrite = cmdString[1]
        client_writeNode(nodeToRead,valueToWrite)
=======
>>>>>>> 13bc130713e5a3a42d1aa0090c8050b29bf9ad96
>>>>>>> Stashed changes
    # if not knownCmd:
    #     unknown_cmd()
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
                addrString = f"{addr}"
                sendString = 'Client ' + addrString + ' says ' + dataString
                sendData = sendString.encode()
                conn.sendall(sendData)
            #print(colored('Remote client says: ','cyan') + stringFromClient)  # THIS LINE KILLS IT