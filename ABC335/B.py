# -*- coding: utf-8 -*-
N = int(input())
for i in range(0,N+1):
    for x in range(0,N+1):
        for z in range(0,N+1):
            if i + x + z <= N:
                print(str(i) + " " + str(x) + " " + str(z) + " " )
