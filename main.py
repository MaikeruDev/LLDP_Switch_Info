from scapy.all import *
from scapy.contrib.lldp import LLDPDU, LLDPDUPortID, LLDPDUSystemName, LLDPDUSystemDescription
import psutil
import os
import sys

def choose_network_adapter():
    adapters = psutil.net_if_addrs()
    adapters_names = [name for name in adapters.keys() if name != 'lo']
    
    print("Please choose a network adapter:")
    for i, adapter in enumerate(adapters_names):
        try:
            ip = [addr for addr in adapters[adapter] if addr.family.name == 'AF_INET'][0].address
        except IndexError:
            ip = "No IP found"
        print(f"{i}. {adapter} - {ip}")
    
    adapter_num = int(input("Please enter the adapter number: "))
    return adapters_names[adapter_num]

def packet_callback(packet):
    if packet.haslayer(LLDPDU):
        port_id_layer = packet.getlayer(LLDPDUPortID)
        system_name_layer = packet.getlayer(LLDPDUSystemName)
        system_description_layer = packet.getlayer(LLDPDUSystemDescription)
        print(f"Port ID: {port_id_layer.id}")
        print(f"System Name: {system_name_layer.system_name}")
        print(f"System Description: {system_description_layer.description}")
 
chosen_adapter = choose_network_adapter()

os.system('cls')
 
sniff(iface=chosen_adapter, prn=packet_callback, filter="ether proto 0x88cc", store=0)
