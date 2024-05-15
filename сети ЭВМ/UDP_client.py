import socket

sock_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv_ip = input("Enter server IP >>> ")
sock_UDP.connect((serv_ip, 5066))

sock_UDP.send('//ready!'.encode())

while True:
    mass = input("You >>> ")
    if mass == "/exit":
        sock_UDP.send(mass.encode())
        break
    else:
        sock_UDP.send(mass.encode())
        mass = (sock_UDP.recv(1024)).decode()
        print(mass)
