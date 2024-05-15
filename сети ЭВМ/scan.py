import socket


def scan_port_TCP(ip, port):
    TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if TCP.connect_ex((ip, port)):
        pass
    else:
        print(f"Port {port} is open")


def scan_port_UDP(ip, port):
    UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    UDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    if UDP.connect_ex((ip, port)):
        print("Error")
    else:
        print(f"Port {port} is open")


domain = input("Enter domain >>> ")
ip = socket.gethostbyname(domain)
rang = input('Enter port range \033[51;34m(ex. "1, 100")\033[0;m >>> ')
indx = rang.find(", ")
rang_1 = int(rang[:indx])
rang_2 = int(rang[indx + 2:]) + 1

print("\033[;33mTCP ports:")
for port_i in range(rang_1, rang_2):
    scan_port_TCP(ip, port_i)

print("\033[;35mUDP ports:")
for port_i in range(rang_1, rang_2):
    scan_port_UDP(ip, port_i)
