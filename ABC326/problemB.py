# -*- coding: utf-8 -*-
N = int(input())
for i in range(N,1001):
    if int(str(i)[0]) * int(str(i)[1]) == int(str(i)[2]):
        print(i)
        exit()
    continue