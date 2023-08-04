# LLDP Port Finder

LLDP Port Finder is a simple Python program that uses the Link Layer Discovery Protocol (LLDP) to identify the switch port that a device is connected to.

## Features

- Easy to use: Just run the program, choose your network adapter, and you'll get your port information instantly.
- Support for all common network adapters.
- No need to physically trace network cables or configure switches.

## Prerequisites

Before you can use LLDP Port Finder, you need to have Python installed on your machine. The program has been tested with Python 3.7, but it should work with other versions as well.

Additionally, you need to install the following Python libraries:

- `scapy`: A powerful Python-based interactive packet manipulation program & library. Scapy supports extensive packet manipulation capabilities which our tool utilises.
- `psutil`: A cross-platform library used to access system details and process utilities. We use it to retrieve network adapter information.
  
To install these libraries, you can use pip:

```
pip install scapy psutil
```

**Note**: Scapy also requires the `WinPcap` network driver to be installed on Windows systems. `WinPcap` is the industry-standard tool for link-layer network access in Windows environments: it allows applications to capture and transmit network packets bypassing the protocol stack, and has additional useful features. You can download it from the [official website](https://www.winpcap.org/install/default.htm).

## How to Use

Using LLDP Port Finder is easy:

1. Clone this repository to your local machine, or download the LLDP Port Finder.py file directly.
2. Open a command prompt or terminal window.
3. Navigate to the directory where you saved LLDP Port Finder.py.
4. Run the command `python LLDP Port Finder.py`.
5. The program will list your network adapters. Choose the adapter that you're interested in by typing its corresponding number and pressing Enter.
6. The program will listen for LLDP packets and display the switch port information when it's received.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
