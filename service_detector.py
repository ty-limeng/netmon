from collections import defaultdict
from services import get_service_name

service_usage = defaultdict(int)

def detect_service(sport, dport, size):
    service = get_service_name(sport)

    if service == "Unknown":
        service = get_service_name(dport)

    service_usage[service] += size

def get_top_services(limit=10):
    return sorted(service_usage.items(), key=lambda x: x[1], reverse=True)[:limit]
