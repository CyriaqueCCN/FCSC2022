from pwn import *

url = "challenges.france-cybersecurity-challenge.fr"
port = 2001

nc = remote(url, port)

def epr(x):
    print(x, end=" ")

LONG_LONG_MAX = 18446744073709551616

for a in range(16):
    x = 9223372036854775808
    found = False
    i = 0
    x_min = 0
    x_max = LONG_LONG_MAX
    print(f"Finding {a}")
    while not found or i > 65:
        #res = nc.readlineS(False) # discard prompt
        #epr(x)
        nc.sendline(str(x).encode())
        res = nc.readlineS(False).strip("> \n")
        #epr(res)
        if res.startswith("+1"):
            x_min = x
            x = x + ((x_max - x) // 2)
            epr("+1")
        if res.startswith("-1"):
            x_max = x
            x = (x + x_min) // 2
            epr("-1")
        if res.startswith("0"):
            found = True
        i += 1
    if found:
        print(nc.readlineS(False))
    else:
        print(f"Not found for x = {x}")

print(nc.readlineS(False))
nc.close()
