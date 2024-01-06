# -*- coding: utf-8 -*-
N, s, K  = map(int,input().split())
QS = []
Qs = []
Ss = []
for i in range(0,N):
    QS.append(input().split())
    temp = tuple(QS[i])
    Qs.append(int(temp[0]))
    Ss.append(int(temp[1]))
Total = 0
for i in range(0,N):
    Total += Qs[i] * Ss[i]
    
if Total >= s:
    print(Total)
else:
    print(Total+K)
              