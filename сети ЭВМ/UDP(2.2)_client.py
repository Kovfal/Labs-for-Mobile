import socket
import threading

sock_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

serv_ip = input("Enter server IP >>> ")
serv_port = int(input("Enter server Port >>> "))
sock_UDP.connect((serv_ip, serv_port))

sock_UDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def lis(sock_UDP):
    while True:
        mass = sock_UDP.recv(1024)
        print('\r' + mass.decode() + "\nYou >>> ", end='')


threading.Thread(target=lis, args=(sock_UDP,), daemon=True).start()

sock_UDP.send('//ready!'.encode())
while True:
    mass = input("You >>> ")
    sock_UDP.send(mass.encode())
