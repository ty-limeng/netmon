# Common service port mappings
PORT_MAP = {
    # Web
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT",
    8443: "HTTPS-ALT",
    8000: "HTTP-DEV",
    8888: "HTTP-DEV",

    # DNS / Network Core
    53: "DNS",
    123: "NTP",
    67: "DHCP",
    68: "DHCP",
    1900: "UPnP",
    5353: "mDNS",

    # Remote Access
    22: "SSH",
    23: "TELNET",
    3389: "RDP",
    5900: "VNC",

    # File Transfer
    20: "FTP-DATA",
    21: "FTP",
    69: "TFTP",
    989: "FTPS-DATA",
    990: "FTPS",
    115: "SFTP",

    # Email
    25: "SMTP",
    465: "SMTPS",
    587: "SMTP-SUBMISSION",
    110: "POP3",
    995: "POP3S",
    143: "IMAP",
    993: "IMAPS",

    # Databases
    1433: "MSSQL",
    1521: "Oracle-DB",
    2049: "NFS",
    2181: "Zookeeper",
    2379: "etcd",
    2483: "Oracle-DB-SSL",
    27017: "MongoDB",
    28017: "MongoDB-Web",
    3000: "Dev-Server",
    3306: "MySQL",
    5432: "PostgreSQL",
    5984: "CouchDB",
    6379: "Redis",
    7001: "WebLogic",
    9042: "Cassandra",

    # Directory / Auth
    389: "LDAP",
    636: "LDAPS",
    1812: "RADIUS",
    1813: "RADIUS-ACCT",

    # Containers / DevOps
    2375: "Docker",
    2376: "Docker-TLS",
    6443: "Kubernetes-API",
    9090: "Prometheus",
    9100: "Node-Exporter",

    # VPN / Tunneling
    500: "IPSec",
    1194: "OpenVPN",
    1701: "L2TP",
    1723: "PPTP",
    41641: "Tailscale",
    51820: "WireGuard",
    7844: "Cloudflare-Tunnel",

    # Messaging / Streaming
    1883: "MQTT",
    5672: "AMQP",
    9092: "Kafka",

    # Gaming / Misc
    25565: "Minecraft",
}

def get_service_name(port):
    return PORT_MAP.get(port, "Unknown")
