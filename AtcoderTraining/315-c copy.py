# -*- coding: utf-8 -*-
N = int(input())
FS = []
for i in range(0,N):
    F, S = map(int,input().split())
    FS.append((F,S))
FS.sort(key=lambda x: x[1],reverse=True)
happiness = []
FirstTuple = FS[0]
NowTuple = ()
for i in range (1,len(FS)):
    NowTuple = FS[i]
    if FirstTuple[0]  == NowTuple[0]:
        happiness.append(FirstTuple[1]+NowTuple[1]/2)
    else:
        happiness.append(FirstTuple[1] + NowTuple[1])
happiness = sorted(happiness, reverse=True)
print(happiness[0])