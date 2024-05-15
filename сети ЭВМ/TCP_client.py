import socket

ser_sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

n = input("Enter your name >>> ")
serv_ip = input("Enter server IP >>> ")
ser_sok.connect((serv_ip, 5060))
ser_sok.send(n.encode())
rec_sok = (ser_sok.recv(1024)).decode()
print(rec_sok, 'is ready!')

while True:
    mass = input(f"{n} >>> ")
    if mass == "/exit":
        ser_sok.send(mass.encode())
        break
    else:
        ser_sok.send(mass.encode())
        mass = (ser_sok.recv(1024)).decode()
        print(f"{rec_sok} >>>", mass)
