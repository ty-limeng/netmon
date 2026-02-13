# Common service port mappings
PORT_MAP = {
    80: "HTTP",
    443: "HTTPS",
    53: "DNS",
    22: "SSH",
    21: "FTP",
    25: "SMTP",
    110: "POP3",
    143: "IMAP",
    3306: "MySQL",
    6379: "Redis",
    8080: "HTTP-ALT",
    123: "NTP",
    67: "DHCP",
    68: "DHCP"
}

def get_service_name(port):
    return PORT_MAP.get(port, "Unknown")
