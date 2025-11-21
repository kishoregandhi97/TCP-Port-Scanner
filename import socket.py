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
    
    s.close()
