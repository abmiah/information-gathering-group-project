import socket   # Used for network operations (DNS resolution, port scanning)
import re       # Used for validating IP addresses
from datetime import datetime # Used for measuring scan time

def is_ip(address):
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(pattern, address) is not None

def ip_to_domain(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "No domain found"

def domain_to_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "No IP found"

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except:
        return False

print("Network Tool (Translate or Scan)")
print("----" * 20)


while True: # Main loop to keep the program running until the user decides to exit
    choice = input("1: Translate IP Domain, 2: Scan ports, 3: Exit → ").strip()

    if choice == "1":
        target = input("Enter IP or domain: ").strip()
        if is_ip(target):
            result = ip_to_domain(target)
            print(f"IP {target} → {result}")
        else:
            result = domain_to_ip(target)
            print(f"Domain {target} → {result}")


    elif choice == "2":
        target_input = input("Enter target (IP/domain): ").strip()
        try:
            target_ip = socket.gethostbyname(target_input)
            print(f"Using {target_ip}")
        except:
            target_ip = target_input
        print("Scanning ports 1-1024...")
        start = datetime.now()
        open_ports = [p for p in range(1, 1025) if scan_port(target_ip, p)]
        end = datetime.now()
        print(f"Open ports: {open_ports}")
        print(f"Time: {end - start}")


    elif choice == "3":
        print("Exiting program!")
        break

    else:
        print("Invalid choice")


if __name__ == "__main__":
    pass