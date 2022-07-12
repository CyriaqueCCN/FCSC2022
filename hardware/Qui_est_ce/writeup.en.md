Let's construct a truth table

```
(x0& !x1) ^x2   y2
0    0    0     0
0    0    1     1
0    1    0     0
0    1    1     1
1    0    0     1
1    0    1     0
1    1    0     0
1    1    1     1
```

Ok we didnt learn anything but that was cool

Well then, we can juste force it
We can guess the values of x61 and x62 (2 possibilities for each)

00
01
10
11

and construct the other bits from them, 1 of the 4 solutions has to be the flag

we do so with solve.py

lo and behold, the flag is the 4th one to print

FCSC{7364529468137835333}
