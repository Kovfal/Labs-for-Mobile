import socket

lis_sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lis_sok.bind(("127.0.0.1", 5011))
lis_sok.listen()

print("Server is ready!")
n = input("Enter your name >>> ")
sok_for_com, add = lis_sok.accept()

cli = (sok_for_com.recv(1024)).decode()
print(cli + " connect!")
sok_for_com.send(n.encode())

while True:
    mass = (sok_for_com.recv(1024)).decode()
    if mass == "/exit":
        print(f"{cli} disconnect!")
        sog = input("Do you want to complete the program? (enter Y/N) >>> ")
        if sog == "Y":
            break
    else:
        print(f"{cli} >>>", mass)
        mass = input(f"{n} >>> ")
        sok_for_com.send(mass.encode())
