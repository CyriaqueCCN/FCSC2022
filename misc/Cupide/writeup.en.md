The "optimal" algorithm greedily solves the backpack problem

If we feed a known non-greedy optimal solution to the input, we will beat it easily

One such solution is :

- possible values : [1, 3, 4]
- goal : 6
- greedy solution : [4, 1, 1]
- optimal solution : [3, 3]

Feeding these values in the right order (6 > 1 2 4 > 3 3) gives the flag

FCSC{bfa26d8861b987d439fe8d8f1004e8b8ea07a7b6f936b844e0f78f43c2dc33e9}
