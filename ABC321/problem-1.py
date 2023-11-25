# -*- coding: utf-8 -*-
N = input()

digits = [int(i) for i in list(N)]


if (int(N) < 10):
    print("Yes")
else:
    i = 0
    for x in digits[:-1]:
        if digits[i] > digits[i+1]:
            i += 1
            continue
        else:
            print("No")
            exit()
    print("Yes")


