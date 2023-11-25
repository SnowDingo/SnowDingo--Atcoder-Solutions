# -*- coding: utf-8 -*-
N = int(input())
As = list(input().split())
x = 0
for i in range(0,len(As)):
    if As[0] == As[i]:
        x += 1
if x == len(As):
    print("Yes")
else:
    print("No")