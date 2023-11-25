# -*- coding: utf-8 -*-
N = int(input())

S = str(input())

i = 0

if S.find("ABC") != -1:
    print(S.find("ABC") +1)
else:
    print(S.find("ABC"))