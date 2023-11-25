# -*- coding: utf-8 -*-
N = int(input())
A, B = map(int, input().split())

sum = 0

digits = []

n = 0
for i in range(N):
    for x in range(N):
        if x > len(str(N)):
            break
        if i[x] + i[x+1] >= A and i[x] + i[x+1] <= B :
            sum += i
            continue
        else:
            continue

print(sum)