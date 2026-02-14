from collections import defaultdict
from services import get_service_name
from stats import LOCAL_IP

flows_upstream = defaultdict(int)
flows_inbound = defaultdict(int)

def update_flow(src, sport, dst, dport, size):

    service = get_service_name(dport)
    if service == "Unknown":
        service = get_service_name(sport)

    # Outbound (server → external)
    if src == LOCAL_IP:
        key = f"{dst}:{dport} ({service})"
        flows_upstream[key] += size

    # Inbound (external → server)
    elif dst == LOCAL_IP:
        key = f"{src}:{sport} ({service})"
        flows_inbound[key] += size


def get_top_upstream(limit=10):
    return sorted(flows_upstream.items(),
                  key=lambda x: x[1],
                  reverse=True)[:limit]


def get_top_inbound(limit=10):
    return sorted(flows_inbound.items(),
                  key=lambda x: x[1],
                  reverse=True)[:limit]
