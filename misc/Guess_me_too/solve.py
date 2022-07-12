#!/usr/bin/env python3

from pwn import *

def odd(x):
    return bin(x).count("1") & 1

def to_bin(l, n_bits):
    return sum([2**i for i in range(n_bits) if l[i] == 1])

def get_error(sec_orig, e_corr, sec_err, i):
    if i > 6:
        return []
    else:
        if odd(sec_orig & e_corr[i]) == sec_err[i]: # error in left half
            return ["1"] + get_error(sec_orig, e_corr, sec_err, i+1)
        else: # error in right half
            return ["0"] + get_error(sec_orig, e_corr, sec_err, i+1)

def change_faulty_bit(s_bits, e):
    s_bits[e] = abs(s_bits[e] - 1)
    return to_bin(s_bits, 128)

def game(nc, payload, e_corr):
    for pl in payload:
        nc.sendline(pl.encode())
    res = nc.readlineS()
    res_l = list(map(int, re.findall("\d+", res)))
    sec_bits = res_l[:128]
    parity = res_l[128]
    sec_err = res_l[129:]
    secret_orig = to_bin(sec_bits, 128)
    # TODO : make this work when the error is on parity
    if parity == odd(secret_orig): # error in last 7 bits, secret_orig is OK
        real_secret = secret_orig
    else: # error in parity or 128 first bits
        err = get_error(secret_orig, e_corr, sec_err, 0)
        err_idx = int("".join(err), 2)
        if err_idx == 127 and False:#odd(): # error in parity, secret_orig is OK
            real_secret = secret_orig
        else: # error in secret_orig, correct it
            real_secret = change_faulty_bit(sec_bits, err_idx)
    nc.sendline(str(real_secret).encode())
    print(nc.readlineS(False))
    rt = nc.readlineS(False).replace(">", "").strip()
    print(rt)
    if rt.startswith("Nope"):
        return 0
    return 1

def main():
    nc = remote("challenges.france-cybersecurity-challenge.fr", 2003)
    bits_at = [str(2**x) for x in range(128)]
    e_corr = []
    e_corr_pl = []
    for i in range(0, 7):
        p = 2 ** i
        r = ("0" * (64 // p) + "1" * (64 // p)) * p
        e = int(r, 2)
        e_corr.append(e)
        e_corr_pl.append(str(e))
    parity = str(int("1" * 128, 2))
    payload = [*bits_at, parity, *e_corr_pl]
    success = 0
    for _ in range(32):
        success += game(nc, payload, e_corr)
    print(f"Success : {success}/32")
    if success == 32:
        print(nc.readlineS())
    nc.close()

main()
