# -*- coding: utf-8 -*-
N = int(input())
As = list(map(int,input().split()))
#List をすべてStrからIntにする
even = []
odd = []
total = []
sumrn = []
for i in As:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd = sorted(odd,reverse=True)
even = sorted(even,reverse=True)
result = -1
if len(even) >= 2:
    result=max(result,even[0] + even[1])
if len(odd)>=2:
    result= max(result,odd[0]+odd[1])
print(result)
