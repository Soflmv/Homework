import socket
import uuid

adress = hex(uuid.getnode())[2:]

for i in range(len(adress)):
    if i % 2 == 1:
        print(f"{adress[-1]}{adress[i]}-", end='')
hostname = socket.gethostname()
adressess = socket.getaddrinfo(hostname, None)
for item in adressess:
    print(item)