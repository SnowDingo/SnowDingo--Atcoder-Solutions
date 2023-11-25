# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
C = int(input())
X = int(input())

answerPattern = 0

for i in range(A+1):
    for x in range(B+1):
        for z in range(C+1):
            if i * 500 + x*100 + z*50 == X:
                answerPattern += 1
                continue
            continue

print(answerPattern)