from pwn import *

url = "challenges.france-cybersecurity-challenge.fr"
port = 2000

nc = remote(url, port)

while nc.connected('any'):
    l = nc.readlineS(False).replace(">", "").strip(" ")
    if l.startswith("Congratulations"):
        flag = nc.readlineS(False)
        print(f"GGWP, {flag}")
        nc.close()
        break
    line = l[::-1]
    nc.sendline(line.encode())
    res = nc.readlineS(False)
    print(f"{l} : {line} ==> {res}")
    if res.startswith("Oops. Bye bye"):# or res.startswith("Congratulations"):
        nc.close()
        break
