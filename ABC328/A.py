# -*- coding: utf-8 -*-
N, X =  map(int, input().split())
Scores = list(input().split())
total = []
for i in range(0,len(Scores)):
    Scores[i] = int(Scores[i])
for i in range(0,len(Scores)):
    if Scores[i] <= int(X):
        total.append(Scores[i])

print(sum(total))