from scapy.all import sniff, IP, TCP, UDP, DNS, DNSQR, ARP, ICMP 
from dns_tracker import update_dns 
from flow_tracker import update_flow 
from stats import update_ip, update_protocol, update_packet 
from service_detector import detect_service 
from device_tracker import update_device

def process_packet(packet):

    # -----------------------------
    # 1. ARP Device Detection
    # -----------------------------
    if packet.haslayer(ARP):
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc
        update_device(ip, mac)
        return


    # -----------------------------
    # 2. Only process IP packets
    # -----------------------------
    if IP not in packet:
        return

    src = packet[IP].src
    dst = packet[IP].dst
    size = len(packet)

    update_ip(src, size)
    update_ip(dst, size)
    update_packet()


    # -----------------------------
    # 3. DNS Detection (UDP 53)
    # -----------------------------
    if packet.haslayer(DNS) and packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode(errors="ignore").rstrip(".")
        update_dns(domain)


    # -----------------------------
    # 4. Protocol + Flow Tracking
    # -----------------------------
    if TCP in packet:
        sport = packet[TCP].sport
        dport = packet[TCP].dport

        update_protocol("TCP")
        update_flow(src, sport, dst, dport, size)
        detect_service(sport, dport, size)

    elif UDP in packet:
        sport = packet[UDP].sport
        dport = packet[UDP].dport

        update_protocol("UDP")
        update_flow(src, sport, dst, dport, size)
        detect_service(sport, dport, size)

    elif ICMP in packet:
        update_protocol("ICMP")
    elif UDP in packet:
        sport = packet[UDP].sport
        dport = packet[UDP].dport
        payload = bytes(packet[UDP].payload)

        update_protocol("UDP")
        update_flow(src, sport, dst, dport, size)

        # QUIC detection via header (first bit often 1 for long header)
        if (sport == 443 or dport == 443 or
            sport == 7844 or dport == 7844) and len(payload) > 0:
            if payload[0] & 0x80:   # QUIC long header flag
                update_protocol("QUIC")

        detect_service(sport, dport, size)

    else:
        update_protocol("Other")
def start_capture(interface=None):
    sniff(
        iface=interface,
        prn=process_packet,
        store=False,
        filter="ip or arp"
    )
