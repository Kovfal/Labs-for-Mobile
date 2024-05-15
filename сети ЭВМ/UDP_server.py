import socket

sock_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_UDP.bind(("127.0.0.1", 5066))
name = input("Enter name of server >>> ")

members = []
while True:
    mass, addr = sock_UDP.recvfrom(1024)
    if addr not in members:
        members.append(addr)

    elif not mass:
        continue

    client_ID = f"{addr[0]}:{addr[1]}"
    if mass.decode() == '//ready!':
        print(f"Client {client_ID} connect!")
        continue

    print(f"Client {client_ID} >>> {mass.decode()}")

    for member in members:
        if member == addr:
            if mass.decode() == "/exit":
                print(f"Client {client_ID} disconnect!")
                sog = input("Do you want to complete the program? (enter Y/N) >>> ")
                if sog == "Y":
                    break
            else:
                mass = input(f"{name} >>> ")
                mass = f"{name} >>> " + mass
                sock_UDP.sendto(mass.encode(), member)
