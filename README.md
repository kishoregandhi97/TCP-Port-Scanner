# TCP-Port-Scanner
import socket

target = input("Enter target IP: ")

print(f"\nScanning target: {target}")
print("-" * 40)

for port in range(1, 1025):    # Scan ports 1–1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)          # Timeout for slow hosts
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} OPEN")
    
    s.close()This project is a beginner-friendly TCP port scanner built using Python’s socket module. It performs a range-based scan (1–1024) and identifies open ports on a target host.
