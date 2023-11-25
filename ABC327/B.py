# -*- coding: utf-8 -*-
B = int(input())
ans = -1
for i in range(0,19):
    if i**i == B:
        ans = i
print(ans)