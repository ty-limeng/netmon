from rich.console import Console
from rich.table import Table
from stats import get_stats
from flow_tracker import get_top_flows
import time
from dns_tracker import get_top_domains
from service_detector import get_top_services
from device_tracker import get_devices
console = Console()

def draw():
    console.clear()

    stats = get_stats()

    console.print("[bold green]Network Monitor[/bold green]\n")

    console.print(f"Bandwidth: {stats['bandwidth'] / 1024:.2f} KB/s")
    console.print(f"Packets/sec: {stats['pps']:.2f}\n")

    ip_table = Table(title="Top IP Traffic")
    ip_table.add_column("IP")
    ip_table.add_column("Bytes")

    for ip, bytes_used in stats["top_ips"]:
        ip_table.add_row(ip, str(bytes_used))

    console.print(ip_table)

    flow_table = Table(title="Top Flows")
    flow_table.add_column("Flow")
    flow_table.add_column("Bytes")
    dns_table = Table(title="Top Domains")
    dns_table.add_column("Domain")
    dns_table.add_column("Queries")
    service_table = Table(title="Service Usage")
    service_table.add_column("Service")
    service_table.add_column("Bytes")
    device_table = Table(title="LAN Devices")
    device_table.add_column("IP Address")
    device_table.add_column("MAC Address")

    for ip, mac in get_devices().items():
        device_table.add_row(ip, mac)

    console.print(device_table)

    for service, usage in get_top_services():
        service_table.add_row(service, str(usage))

    console.print(service_table)

    for domain, count in get_top_domains():
        dns_table.add_row(domain, str(count))

    console.print(dns_table)

    for flow, bytes_used in get_top_flows():
        flow_table.add_row(flow, str(bytes_used))

    console.print(flow_table)

def start_dashboard():
    while True:
        draw()
        time.sleep(1)
