from collections import defaultdict

dns_queries = defaultdict(int)

def update_dns(domain):
    dns_queries[domain] += 1

def get_top_domains(limit=10):
    return sorted(dns_queries.items(), key=lambda x: x[1], reverse=True)[:limit]
