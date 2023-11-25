# -*- coding: utf-8 -*-
N, Q =  map(int, input().split())
S = str(input())
Ls = ()
# Ss = Sを配列か%１文字筒ばらしたもの
Ss = []
for i in range(0,Q):
    Ls = Ls + tuple(map(int,input().split()))
for i in range(0,N):
    Ss.append(S[i])

for questionId in range(0,Q):
    score = 0
    for CurrentNumber in range(Ls[questionId*2],Ls[questionId*2+1]+1):
        if CurrentNumber != N-1:
            if str(S[CurrentNumber]) == str(S[CurrentNumber+1]):
                score += 1
        if CurrentNumber > 1:
            if str(S[CurrentNumber]) == str(S[CurrentNumber-1]):
               score += 1
    print(score)