from pwn import *

def odd(x):
    return bin(x).count("1") & 1

def to_bin(l, n_bits):
    return sum([2**i for i in range(n_bits) if l[i] == 1])

def get_error(sec_orig, e_corr, sec_err, i):                 
    if i > 6:                                                          
        return []
    else:
        if odd(sec_orig & e_corr[i]) == sec_err[i]:
            # erreur moitie gauche
            return ["1"] + get_error(sec_orig, e_corr, sec_err, i+1)
        else:
            return ["0"] + get_error(sec_orig, e_corr, sec_err, i+1)

def change_faulty_bit(s_bits, err):
    e = int("".join(err), 2)#to_bin(err, 7) - 1
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
    
    # TODO : make this work
    #if error_in_correction(secret_orig, sec_err, e_corr, parity):
    #    real_secret = secret_orig
    #else:
    #    err = get_error(secret_orig, e_corr, sec_err, 0)
    #    real_secret = change_faulty_bit(sec_bits, err)
    
    #if parity == odd(secret_orig): # error in last 7 bits, secret_orig is OK
    #    real_secret = secret_orig
    #else:
    err = get_error(secret_orig, e_corr, sec_err, 0)
        #if err == 85 and ???: # error in parity, secret_orig is OK
        #    real_secret = secret_orig
        #else: # error in secret_orig, correct it
    real_secret = change_faulty_bit(sec_bits, err)
    #print(f"{secret_orig=}\n{real_secret=}")
    
    nc.sendline(str(real_secret).encode())
    print(nc.readlineS(False))
    rt = nc.readlineS(False).replace(">", "").strip()
    print(rt)
    if rt.startswith("Nope"):
        return 0
    return 1

def main():
    nc = remote("challenges.france-cybersecurity-challenge.fr", 2003)
    # generate the 'bits_at' array : each entry will give 1 bit pos from the secret
    bits_at = [str(2**x) for x in range(128)]
    # generate the error correction array : each entry is a step to a dichotomy search of the secret number
    e_corr_pl = ["1" * 128]
    for i in range(0, 7):
        p = 2 ** i
        r = ("0" * (64 // p) + "1" * (64 // p)) * p
        e_corr_pl.append(str(int(r, 2)))
    e_corr = [int(s) for s in e_corr_pl[1:]]
    payload = [*bits_at, *e_corr_pl]
    success = 0
    for _ in range(32):
        success += game(nc, payload, e_corr)
    print(f"Success : {success}/32")
    if success == 32:
        print(nc.readlineS())
    nc.close()

main()
