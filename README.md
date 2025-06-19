# arduino-opta-tcp-socket
Python code to communicate with Arduino Opta PLC running OPC UA server with TCP socket.

Purpose:
- Allow remote control of [Arduino Opta PLC](https://www.arduino.cc/pro/hardware-arduino-opta/) and connected expansion modules via TCP socket over Ethernet with Python.
- Compatibility with [SICS](http://lns00.psi.ch/sics/design/sics.html). 

## First iteration
To start, a Python client and Python server to communicate via TCP socket on same computer (loopback). 

Purpose:
- Establish reliable two-way communication between client and server using TCP socket.
- Have server interpret user commands in a useful way for controlling an Arduino Opta PLC.
- Implement some error handling before actual hardware is involved. 

## Second iteration
Python client on computer talks to Python server via TCP on same computer, and TCP server talks to Arduino Opta via Ethernet using OPC UA.

Purpose:
- Introduce communication with Arduino Opta PLC running OPC UA server.


## Third iteration
Python client on computer talks to Python server on Arduino Portenta or similar running microphython, which talks to Arduino Opta via Ethernet using OPC UA.

Purpose:
- Eliminate need for a computer to act as the Python server for communication with the Arduino Opta PLC. 

## Final iteration
SICS client talks to Python server on Arduino Portenta or similar running micropython, which talks to Arduino Opta via Ethernet using OPC UA.

## Dependencies

The following packages are required on top of a basic miniconda install:
- opcua
- opcua-client
- 

## How to set it up

