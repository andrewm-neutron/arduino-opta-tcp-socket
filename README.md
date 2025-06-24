# arduino-opta-tcp-socket
Python code to communicate with Arduino Opta PLC running an [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) server with TCP socket.

Purpose:
- Allow remote control of [Arduino Opta PLC](https://www.arduino.cc/pro/hardware-arduino-opta/) and connected expansion modules via TCP socket over Ethernet with Python.
- Compatibility with [SICS](http://lns00.psi.ch/sics/design/sics.html).
- Written using [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main).

## First iteration
To start, a Python client and Python server to communicate via TCP socket on same computer (loopback). Following from this [Real Python article](https://realpython.com/python-sockets/) to build an echo client and server.

Purpose:
- Establish reliable two-way communication between client and server using TCP socket.
- Have server interpret user commands in a useful way for controlling an Arduino Opta PLC.
- Implement some error handling before actual hardware is involved.

To run:
- Open and run `echo-server-andrewm.py` first.
- Then open and run `echo-client-andrewm.py`.
- Type commands into the latter, and see the former respond. 

## Second iteration
Python client on computer talks to Python server via TCP on same computer, and TCP server talks to Arduino Opta via Ethernet using [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/).

Purpose:
- Introduce communication with Arduino Opta PLC running OPC UA server.


## Third iteration
Python client on computer talks to Python server on Arduino Portenta or similar running [microphython](https://micropython.org/), which talks to Arduino Opta via Ethernet using OPC UA.

Purpose:
- Eliminate need for a computer to act as the Python server for communication with the Arduino Opta PLC. 

## Final iteration
SICS client talks to Python server on Arduino Portenta or similar running micropython, which talks to Arduino Opta via Ethernet using OPC UA.

## Dependencies

The following packages are required on top of a basic miniconda environment (`pip install ...` in miniconda prompt terminal):
- opcua
- opcua-client
- crypto
- cryptography
- termcolor
- numpy
- pandas
- pyqtgraph (for OPC-UA client)
- spyder-kernels==3.0.* (If using Spyder as IDE)

## How to edit and run the Python client and server

To get it working:
- Install [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) and create an environment with the packages listed under the dependencies (or your preferred alternative).
- Install a Python IDE such as [Spyder](https://www.spyder-ide.org/).
- Follow the [Arduino Opta PLC tutorial](https://opta.findernet.com/en/tutorial/user-manual#opc-unified-architecture-opc-ua-32) up to and including the section about OPC-UA. Key outcomes of this are:
  - Install [Arduino IDE](https://www.arduino.cc/en/software/) and use the Library Manager to install each of the packages described in the tutorial (Opta core - Arduino mbed OS Opta Boards, arduino_json, arduinoBLE (Bluetooth - useful for testing but not necessary), arduino_OPC_UA, portentaEthernet, optaBlue, mbed_rtc_time).
  - Assemble the Opta PLC and expansion modules (up to two modules supported by OPC-UA), and test as required with [Arduino PLC IDE](https://www.arduino.cc/pro/software-plc-ide/). 
  - Upload [Arduino Opta OPC-UA server sketch](https://github.com/arduino-libraries/Arduino_OPC_UA/blob/main/examples/opta_opcua_server/opta_opcua_server.ino) to the PLC.
  - Use [PuTTY](https://www.putty.org/) or similar to check communications with the OPC-UA server running on the PLC. Communicate via Serial on the COM port used in the Arduino IDE (in this case, COM3), at speed 9600. This should also report the IP address for the OPC-UA server running on the Arduino Opta. This local IP address can also be found from your router or `arp -a`, and note that the address derived from the Ethernet tutorial for the Opta PLC will be for the WAN connection and not the local LAN.  
    
    <img src="https://github.com/user-attachments/assets/c2ff14ae-2231-4002-aa01-bd4973b49ec2" width=50% height=50%>
    <img src="https://github.com/user-attachments/assets/ee74186e-2143-40ec-9a18-472fdf765440" width=75% height=75%>
  - Find the `opcua-client` installed via pip, default path for miniconda3 on Windows is `C:\Users\<UserName>\miniconda3\envs\<EnvName>\Scripts\opcua-client.exe`, and launch the executable.
  - In the address bar, type `opc.tcp://<IPaddress>:4840`. Note that the command window for the client lists the active OPC-UA servers running, including the localhost and any server simulators being used such as [the Integration Objects OPC-UA Server Simulator](https://integrationobjects.com/sioth-opc/sioth-opc-unified-architecture/opc-ua-server-simulator/). This can be used to explore the configuration of the PLC and to identify the relevant [NodeId values](https://opcua-asyncio.readthedocs.io/en/latest/usage/common/node-nodeid.html) of the controller and attached modules. Note that other connections to the OPA-UA server such as through the Arduino IDE must be closed first.
    <img src="https://github.com/user-attachments/assets/fef9b096-8d0a-456a-ab91-27eaac563fa8" width=75% height=75%>

