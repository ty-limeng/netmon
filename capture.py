from scapy.all import sniff, IP, TCP, UDP, DNS, DNSQR
from dns_tracker import update_dns
from flow_tracker import update_flow
from stats import update_ip, update_protocol, update_packet

def process_packet(packet):
    # DNS detection
    if packet.haslayer(DNS) and packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode(errors="ignore").rstrip(".")
        update_dns(domain)

    if IP not in packet:
        return

    src = packet[IP].src
    dst = packet[IP].dst
    size = len(packet)

    update_ip(src, size)
    update_ip(dst, size)
    update_packet()

    if TCP in packet:
        sport = packet[TCP].sport
        dport = packet[TCP].dport
        update_protocol("TCP")
        update_flow(src, sport, dst, dport, size)

    elif UDP in packet:
        sport = packet[UDP].sport
        dport = packet[UDP].dport
        update_protocol("UDP")
        update_flow(src, sport, dst, dport, size)

    else:
        update_protocol("Other")

def start_capture(interface=None):
    sniff(
        iface=interface,
        prn=process_packet,
        store=False,
        filter="ip"
    )
