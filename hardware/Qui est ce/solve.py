
# y0 = x0 ^ (~x62 & x61)
# y1 = x1 ^ (~x0 & x62)
# etc

# reverse :
# x0 impacts y0, y1 and y2
# x1 impacts y1, y2 and y3
# x2 impacts y2, y3 and y4
# x3 impacts y3, y5 and y5
# so y3 is impacted by x1, x2 and x3
# logical table
# compute yx, yz... then infer result

def get_y(x, i):
    if i == 0:
        xm1 = (x >> 62) & 1
        xm2 = (x >> 61) & 1#x & (2**61)
    elif i == 1:
        xm2 = (x >> 62) & 1#x & (2**62)
        xm1 = x & 1
    else:
        xm2 = (x >> (i-2)) & 1#x & (2**(i-2))
        xm1 = (x >> (i-1)) & 1#x & (2**(i-1))
    xi = (x >> i) & 1#x & (2**i)
    if (xm2 & ~xm1) ^ xi:
        return 2**i
    return 0

def oneway(x):
    y = 0
    for i in range(63):
        y += get_y(x, i)
    return y

def get_x(y, i):
    return 1

def twoway(y):
    x = 0
    for i in range(63):
        x += get_x(y, i)
    return x

test_oneway = 6497282320360345885
test_twoway = 1333333333333333337
flag_y = 8549048879922979409
#print(oneway(test_oneway))
print("FCSC{" + str(twoway(test_twoway)) + "}")
