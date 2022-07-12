#!/usr/bin/env python3

# python3 -m pip install pycryptodome
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

def original():
    print("Enter your password")
    password = input(">>> ").encode()
    h = HMAC.new(password, digestmod = SHA256)
    h.update(b"FCSC2022")
    
    iv = get_random_bytes(16)
    k  = SHA256.new(password).digest()
    c  = AES.new(k, AES.MODE_CBC, iv = iv).encrypt(pad(open("flag.txt", "rb").read(), 16))
    r = {
        "iv": iv.hex(),
        "c": c.hex(),
        "h": h.hexdigest(),
    }
    open("output.txt", "w").write(json.dumps(r))


iv = bytes.fromhex("ea425b2ea4bb67445abe967e3bd1b583")
c = bytes.fromhex("69771c85e2362a35eb0157497e9e2d17858bf11492e003c4aa8ce1b76d8d3a31ccc3412ec6e619e7996190d8693299fc3873e1e6a96bcc1fe67abdf5175c753c09128fd1eb2f2f15bd07b12c5bfc2933")

pwd = "omgh4xx0r".encode()
k = SHA256.new(pwd).digest()
gg = AES.new(k, AES.MODE_CBC, iv=iv)
xd = gg.decrypt(c)
print(xd)
