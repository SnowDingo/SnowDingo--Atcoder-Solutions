# -*- coding: utf-8 -*-

S = int(input())

digits = [int(i) for i in list(str(S))]

number = 0
for i in digits:
    if i == 1:
        number += 1
    else:
        continue

print(number)