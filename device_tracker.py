devices = {}

def update_device(ip, mac):
    if ip not in devices:
        devices[ip] = mac

def get_devices():
    return devices
