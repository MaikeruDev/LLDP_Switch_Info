import tkinter as tk
from scapy.all import *
from scapy.contrib.lldp import LLDPDU, LLDPDUPortID, LLDPDUSystemName, LLDPDUSystemDescription
import psutil
import os
import sys


def choose_network_adapter():
    adapters = psutil.net_if_addrs()
    adapters_info = []
    for name in adapters.keys():
        if 'eth' in name or 'Ethernet' in name:
            try:
                ip = [addr for addr in adapters[name] if addr.family.name == 'AF_INET'][0].address
            except IndexError:
                ip = "Keine IP gefunden"
            adapters_info.append(f"{name} - {ip}")
    
    adapter_list.set(tuple(adapters_info))  

def packet_callback(packet):
    if packet.haslayer(LLDPDU):
        port_id_layer = packet.getlayer(LLDPDUPortID)
        system_name_layer = packet.getlayer(LLDPDUSystemName)
        system_description_layer = packet.getlayer(LLDPDUSystemDescription)
        port_id.set(f"Port ID: {port_id_layer.id}")
        system_name.set(f"System Name: {system_name_layer.system_name}")
        system_description.set(f"System Description: {system_description_layer.description}")
        return True


def start_sniffing():
    selected_adapter = lb.get(lb.curselection()).split(" - ")[0]
    sniff(iface=selected_adapter, prn=packet_callback, filter="ether proto 0x88cc", store=0, stop_filter=packet_callback)


root = tk.Tk()
 
root.minsize(300, 200)
 
root.title("Switch sniffing")
 
adapter_list = tk.Variable()
port_id = tk.StringVar()
system_name = tk.StringVar()
system_description = tk.StringVar()
 
lb = tk.Listbox(root, listvariable=adapter_list)
btn = tk.Button(root, text="Start Sniffing", command=start_sniffing)
lbl_port_id = tk.Label(root, textvariable=port_id)
lbl_system_name = tk.Label(root, textvariable=system_name)
lbl_system_description = tk.Label(root, textvariable=system_description)
 
lb.pack(fill=tk.BOTH, expand=1)
btn.pack()
lbl_port_id.pack()
lbl_system_name.pack()
lbl_system_description.pack()
 
choose_network_adapter()

root.mainloop()
