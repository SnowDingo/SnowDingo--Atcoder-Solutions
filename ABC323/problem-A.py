# -*- coding: utf-8 -*-
even = [2,4,6,8,10,12,14,16]
S = input()
score = 0
x = 0
for i in even:
    if S[i-1] == "0":
        score += 1
        continue
    else:
         continue

if score == len(even):
    print("Yes")
    exit()
else:
    print("No")
    exit()