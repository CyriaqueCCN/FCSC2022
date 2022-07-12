We see that the flag was shuffled with a random seed between 0 and 256

So we try to reverse the shuffle for each seed and printing the result if it starts with our beloved "FCSC{"

(reversing the shuffle for a given seed implies to create a new shuffled list with indexes 1-len(list) and using it to get which index was moved at which place)

flag is 

FCSC{d93d32485aec7dc7622f13cd93b922363911c36d2ffd4f829f4e3264d0ac6952}
