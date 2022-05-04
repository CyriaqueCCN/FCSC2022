# F = a, f, g, e
# C = a, f, e, d
# S = a, f, g, c, d
# 2 = a, b, g, e, d
# 0 = a, f, e, d, b, c
# 2.= a, b, g, e, d, dp

F    = "000111110"
C    = "100111100"
S    = "110101110"
two  = "101110110"
twod = "101110111"
zero = "111111100"

r = F + C + S + C + two + zero + two + twod
print("FCSC{" + r + "}")
