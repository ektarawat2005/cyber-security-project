import socket

target = input("Enter target (example: google.com): ")

print("\nScanning started...\n")

for port in range(20, 100):
    s = socket.socket()
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        print(f"Port {port} is OPEN")
    except:
        pass

    s.close()

print("\nScan complete ✅")