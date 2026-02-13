from collections import defaultdict
from services import get_service_name

flows = defaultdict(int)

def update_flow(src, sport, dst, dport, size):
    # detect service from either port
    service = get_service_name(sport)
    if service == "Unknown":
        service = get_service_name(dport)

    # ntop-style flow format
    if service != "Unknown":
        key = f"{src}:{sport} ({service}) -> {dst}:{dport}"
    else:
        key = f"{src}:{sport} -> {dst}:{dport}"

    flows[key] += size

def get_top_flows(limit=10):
    return sorted(flows.items(), key=lambda x: x[1], reverse=True)[:limit]
