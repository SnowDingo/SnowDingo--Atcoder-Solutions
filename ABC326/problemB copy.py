# -*- coding: utf-8 -*-
N,M = map(int,input().split())
As = list(input().split())
As = [int(i) for i in As]
As = sorted(As)
x = As[0]
maxX = x + float(M)
gifts= []
rightnow = []
for z in range(As[0],len(As)):
    for i in range(0,N):
        if As[i] >= x and As[i] < maxX:
            rightnow.append(As[i])
    x = As[z]
    maxX = x + M
    gifts.append(len(rightnow))
    rightnow = []
gifts= sorted(gifts,reverse=True)
if len(gifts) > 0 :
    print(gifts[0])
else:
    number = 0
    num = []
    for i in range(0,len(As)-1):
        my_dict = {i:As.count(As[i]) for i in As}
    print(list(my_dict.values())[0])
                