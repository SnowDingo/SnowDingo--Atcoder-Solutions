# -*- coding: utf-8 -*-
N = int(input())
WX = {}
for i in range(0,N):
    W,X = map(int,input().split())
    WX[W] = X
print(WX)
availableperson = []
max = []

for time in range (9,19):
    availableperson = []
    for i in range(0,len(WX)):
        WX.keys = list(WX.keys)[i] + time
    for x in range(0,len(WX.keys)):
        if WX.keys[x] > 18 or WX.keys[x] < 9:
            continue
        else:
            availableperson.append(WX.values[x])
    max.append(sum(availableperson))