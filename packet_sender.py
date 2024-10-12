#!/usr/bin/env python

from scapy.all import *

def send_packets(destination_ip, packet_id):
    # Create the packet
    packet = IP(dst=destination_ip, id=packet_id, ttl=99) / TCP(sport=RandShort(), dport=[22], seq=12345, ack=1000, window=1000, flags="S") / "HaX0r SVP"
    
    # Display the packet structure
    print("Packet Fields:")
    ls(packet)
    
    # Sending packets in 0.3 second intervals with a timeout of 4 seconds
    print("Sending packets in 0.3 second intervals...")
    ans, unans = srloop(packet, inter=0.3, retry=5, timeout=4)
    
    # Displaying summary of sent and unanswered packets
    print("Answered packets:")
    ans.summary()
    
    print("Unanswered packets:")
    unans.summary()
    
    # Display source port and flags
    print("Source port and flags:")
    ans.make_table(lambda s, r: (s.dst, s.dport, r.sprintf("%IP.src%\t%IP.dst%\t%TCP.flags%")))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python packet_sender.py <destination_ip> <packet_id>")
        sys.exit(1)
    
    destination_ip = sys.argv[1]
    packet_id = int(sys.argv[2])
    
    send_packets(destination_ip, packet_id)
