from collections import defaultdict

flows = defaultdict(int)

def update_flow(src, sport, dst, dport, size):
    key = f"{src}:{sport} -> {dst}:{dport}"
    flows[key] += size

def get_top_flows(limit=10):
    return sorted(flows.items(), key=lambda x: x[1], reverse=True)[:limit]
