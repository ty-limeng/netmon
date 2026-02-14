from collections import defaultdict
import time
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

LOCAL_IP = get_local_ip()

ip_traffic = defaultdict(int)
protocol_count = defaultdict(int)

total_bytes = 0
packet_count = 0
start_time = time.time()

def update_ip(ip, size):
    global total_bytes
    ip_traffic[ip] += size
    total_bytes += size

def update_protocol(proto):
    protocol_count[proto] += 1

def update_packet():
    global packet_count
    packet_count += 1

def get_stats():
    elapsed = time.time() - start_time
    return {
        "bandwidth": total_bytes / elapsed if elapsed else 0,
        "pps": packet_count / elapsed if elapsed else 0,
        "top_ips": sorted(ip_traffic.items(), key=lambda x: x[1], reverse=True)[:5],
        "protocols": dict(protocol_count)
    }
