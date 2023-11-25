# -*- coding: utf-8 -*-
N, M = map(int, input().split())
B = []
B.append(input().split())
A = [int(i) for i in list(int(B))]
i = 1
x = 0
for i in range(1,N+1):
    if i == A[x]:
        print(0)
        x += 1
        continue
    else:
        print(A[x]-i)
        continue