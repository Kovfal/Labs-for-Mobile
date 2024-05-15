import socket

sock_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock_UDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
serv_port = int(input("Enter server Port >>> "))
sock_UDP.bind(("255.255.255.255", serv_port))

memb = []
while True:
    mass, addr = sock_UDP.recvfrom(1024)

    if addr not in memb:
        memb.append(addr)

    elif not mass:
        continue

    client_ID = f"{addr[0]}:{addr[1]}"
    if mass.decode() == '//ready!':
        print(f"Client {client_ID} connect!")
        continue

    mass = f"Client {client_ID} >>> {mass.decode()}"

    for member in memb:
        if member == addr:
            continue

        sock_UDP.sendto(mass.encode(), member)
