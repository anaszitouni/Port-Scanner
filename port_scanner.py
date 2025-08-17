import socket
import re


# Basic user interface header
print(r"""   ________  __________________   ___________    ________
  / ____/ / / / ____/ ____/  _/  / ____/  _/ |  / / ____/
 / / __/ / / / /   / /    / /   / /_   / / | | / / __/
/ /_/ / /_/ / /___/ /____/ /   / __/ _/ /  | |/ / /___
\____/\____/\____/\____/___/  /_/   /___/  |___/_____/""")

# Info ta3 copyright
print("\n****************************************************************")
print("\n* Copyright of Gucci Five, 2025                              *")
print("\n* https://www.instagram.com/anas_zitouni                     *")
print("\n****************************************************************")

# Ask user to input ip address or domain they want to scan
while True:
    ip = input("\nPlease Enter the IP address or domain that you want to scan: ") # katsawal user yktb IP/domain
    try:
        resolved_ip = socket.gethostbyname(ip)     # kat7awl domain l IP; ila fashaL kay3ti exception
        print(f"✅ Resolved IP: {resolved_ip}")     # katprinti l-IP li tla3
        break                                      # ila kolchi mzyan, katkhrj mn loop
    except socket.gaierror:
        print("❌ Invalid IP address or domain. Please try again.\n")  # ila kan ghalat, kat3awd ttsawl

# Daba katsawal user 3la range dyal ports li bgha yscanihom
while True:
    print("\nPlease enter the range of ports you want to scan in format: <int>-<int> (e.g., 60-120)")
    port_range = input("\nPlease Enter the ports range: ") # input dyal user
    
    match = re.match(r"^\s*(\d+)\s*-\s*(\d+)\s*$", port_range) # regex bash njib start w end mn l-input
    
    if match:
        port_min = int(match.group(1))              # l-port l-sghir
        port_max = int(match.group(2)) + 1          # l-port l-kbir (+1 bash ydkhl f range)
        if 0 <= port_min <= 65535 and 0 <= port_max <= 65536:  # check wach ports validin f range 0-65535
            break                                   # ila valid, nkhrj mn loop
        else:
            print("❌ Port numbers must be between 0 and 65535.\n")  # ports kharjin 3la l-range
    else:
        print("❌ Invalid format. Please use the format like 20-80.\n")  # format ghalat

# Katprinti l-info dyal scan
# Begin port scan
print(f"\nScanning {ip} from port {port_min} to {port_max - 1}...\n")

# loop 3la kol port f range
for port in range(port_min, port_max):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # katsift socket TCP
    s.settimeout(0.1)   # timeout sghira (0.1 sec) bash l-scan ykon s3ib w maytwalch
    result = s.connect_ex((ip, port))   # katsift request l-port

    if result == 0:     # ila l-port ma-mesdoudch (open)
        try:
            service = socket.getservbyport(port)   # katsawal 3la ism l-service (e.g., HTTP, FTP...)
        except:
            service = "Unknown"     # ila l-port ma3rufch, kaydir "Unknown"
        print(f"[OPEN] Port {port} - Service: {service}")   # kay7t linfo dyal lport li l9ah m7lol
    # Optional: Uncomment to show closed ports
    # else:
       # print(f"[CLOSED] Port {port}")

    s.close()   # katsd socket