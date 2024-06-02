import subprocess

def get_connected_devices():
    output = subprocess.check_output(["sudo", "arp", "-a"])
    devices = {}
    for line in output.splitlines():
        if "(" in line:
            split_line = line.split("(")
            ip = split_line[0].strip()
            mac = split_line[1].strip(")").replace(" ", ":")
            devices[ip] = mac
    return devices

print(get_connected_devices())
