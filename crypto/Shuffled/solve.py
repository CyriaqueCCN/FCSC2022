#!/usr/bin/env python3

import random

rl = list("f668cf029d2dc4234394e3f7a8S9f15f626Cc257Ce64}2dcd93323933d2{F1a1cd29db")

# thanks to crypto SO
def unshuffle_list(shuffled_ls, seed):
  n = len(shuffled_ls)
  shuffled_perm = [i for i in range(1, n + 1)]
  random.shuffle(shuffled_perm)
  ls = list(zip(shuffled_ls, shuffled_perm))
  ls.sort(key=lambda x: x[1])
  return [a for (a, b) in ls]

for seed in range(257):
    random.seed(seed)
    res = unshuffle_list(rl, seed)
    sres = "".join(res)
    if sres.startswith("FCSC"):
        print(sres)
