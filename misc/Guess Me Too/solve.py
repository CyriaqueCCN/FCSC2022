from pwn import *

url = "challenges.france-cybersecurity-challenge.fr"
port = 2003

nc = remote(url, port)

for a in range(1, 137):
    nc.sendline(str(a).encode())

print(nc.readlineS())
print(nc.readlineS())
print(nc.readlineS())
nc.close()
