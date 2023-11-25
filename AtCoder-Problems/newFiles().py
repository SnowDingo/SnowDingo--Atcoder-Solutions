# -*- coding: utf-8 -*-
N = int(input())
Ss = []
for i in range(N):
    Ss.append(str(input()))
#すでに登場した単語をここに登録
already = []
for i in range(0,len(Ss)):
    x = 0
    for x in range(0,len(Ss)):
        print(x)
        if Ss[i] in already != True:
            already.append(Ss[i])
            continue
        else:
            Ss[i] = Ss[i]+str(x)
            continue
print(Ss)