# wids.py

from scapy.all import *
import logging

# Configure logging
logging.basicConfig(filename='rogue_aps.log', level=logging.INFO)

# List of authorized APs
authorized_aps = [
    "00:11:22:33:44:55",  # Replace with your authorized AP MACs
    "66:77:88:99:AA:BB"
]

def packet_handler(packet):
    if packet.haslayer(Dot11) and packet.type == 0 and packet.subtype == 8:  # Beacon frame
        ssid = packet[Dot11].info.decode('utf-8', errors='ignore')
        mac = packet[Dot11].addr2
        if mac not in authorized_aps:
            print(f"Rogue AP detected! SSID: {ssid}, MAC: {mac}")
            logging.info(f"Rogue AP detected! SSID: {ssid}, MAC: {mac}")

def start_sniffing():
    print("Starting to sniff on wlan0...")
    sniff(iface='wlan0', prn=packet_handler, store=0)

if __name__ == '__main__':
    start_sniffing()
