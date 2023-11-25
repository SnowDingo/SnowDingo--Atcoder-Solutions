# -*- coding: utf-8 -*-
N = int(input())
M = N
while True:
    if M%2==0:
        M = M/2
        continue
    else:
        break
while True:
    if M%3 == 0:
        M = M/3
        continue
    else:
        break
if M == 1:
    print("Yes")
else:
    print("No")
    