# -*- coding: utf-8 -*-
K = int(input())

number321 = 0
number = 1

def checknumber(N):
    digits = [int(i) for i in list(str(N))]
    if (int(N) < 10):
        return True
    else:
        i = 0
        for x in digits[:-1]:
            if digits[i] <= digits[i+1]:
                return False
            i = i + 1
        return True   

while K != number321:
    if checknumber(number):
        number += 1
        number321 += 1
    else:
        number += 1
print(number-1)

