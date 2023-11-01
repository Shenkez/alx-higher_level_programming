#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i == j or j < i:
            pass
        elif j == 9 and i == 8:
            print("{}{}".format((i), (j)))
        else:
            print("{}{},".format((i), (j)), end=" ")
