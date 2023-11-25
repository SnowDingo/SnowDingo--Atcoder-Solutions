# -*- coding: utf-8 -*-
N = int(input())
Fs = []
Ss = []
for i in range(0,N):
    F, S = map(int,input().split())
    Fs.append(F)
    Ss.append(S)
FsSs = {}
happines = []
for i in range(0,len(Fs)-1):
    for x in range(0,len(Ss)-1):
        print("-"+str(Fs[i]) + " " + str(Fs[x+1]))
        if Fs[i] != Fs[x+1]:
            happines.append(Ss[i]+ Ss[x+1])
        elif Fs[i] == Fs[x+1]:
            happines.append(Ss[i] + (Ss[x+1]/2))
happines = sorted(happines,reverse=True)
print(happines)