def get_y(x, i):
    if i == 0:
        xm1 = (x >> 62) & 1
        xm2 = (x >> 61) & 1  # x & (2**61)
    elif i == 1:
        xm2 = (x >> 62) & 1  # x & (2**62)
        xm1 = x & 1
    else:
        xm2 = (x >> (i - 2)) & 1  # x & (2**(i-2))
        xm1 = (x >> (i - 1)) & 1  # x & (2**(i-1))
    xi = (x >> i) & 1  # x & (2**i)
    if (xm2 & ~xm1) ^ xi:
        return 2**i
    return 0


def oneway(x):
    y = 0
    for i in range(63):
        y += get_y(x, i)
    return y


# y0 = x0 ^ (~x62 & x61)
# y1 = x1 ^ (~x0 & x62)


def get_x(to_find, bits, i, x61, x62):
    sec_x = bin(to_find & (2**i)).count("1") & 1
    if i == 0:
        return sec_x ^ (x61 & ~x62)
    if i == 1:
        return sec_x ^ (x62 & ~bits[0])
    return sec_x ^ (bits[i - 2] & ~bits[i - 1])


def from_bits(b):
    return sum([2**i for i in range(len(b)) if b[i] == 1])


def build_from(to_find, x61, x62):
    # we assume x0 and x1 have a fixed value
    bits = []
    for i in range(61):
        r = get_x(to_find, bits, i, x61, x62)
        bits.append(r)
    bits.append(x61)
    bits.append(x62)
    return from_bits(bits)


test_x = 6497282320360345885
# test_y = 1333333333333333337
flag_y = 8549048879922979409
# print(oneway(test_x))
print("FCSC{" + str(build_from(flag_y, 0, 0)) + "}")
print("FCSC{" + str(build_from(flag_y, 0, 1)) + "}")
print("FCSC{" + str(build_from(flag_y, 1, 0)) + "}")
print("FCSC{" + str(build_from(flag_y, 1, 1)) + "}")
