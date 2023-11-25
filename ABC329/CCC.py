# -*- coding: utf-8 -*-
#NはSのながさ
N = int(input())
#Sは文字列
S = str(input())
#既に使われている文字列を収納
already = []
#1010101
sumup = []
n = 1

def true(n):
    for i in range(0,len(n)-1):
        if n[i] == n[i+1]:
            return True
#編集
for i in range(0,N-2):
    #XはIより１大きい
    x = i+1
    wrong = 0
    while wrong == 0:
        #もし最大値の場所にある文字と今調べている文字が同じならー＞
        if S[i] == S[x] and S[i] + S[i:x]  not in already:
                n += 1
                x += 1
                already.append(S[i] + S[i:x])
                continue
        else:
             wrong += 1
             break

    if S[i] != S[x] and S[i] not in already:
        n += 1
        already.append(S[i])
    else:
        n += 0
Ss = list(already)
for z in range(0,len(Ss)-2):
     for x in range(0,len(Ss)-2):
        if Ss[z] == Ss[x]:
            Ss.remove(Ss[x])
print(Ss)