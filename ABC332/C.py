# -*- coding: utf-8 -*-
N, M = map(int,input().split())
S = str(input())
Days = []
for i in range(0,N):
    Days.append(int(S[i]))
amountNeeded = 0
if M == 0:
    amountNeeded += 1

while True:
    dirty = 0
    normal = M
    special = amountNeeded
    clean = normal + amountNeeded
    gameover = False
    if amountNeeded + normal <= N:
        for i in range(0,N):
            if Days[i] == 0:
                dirty=0
                normal = M
                special = amountNeeded
            elif Days[i] == 1:
                if normal ==0 and special > 1:
                    dirty+=1
                    special -= 1
                elif normal == 0 and special == 0:
                    gameover = True
                    break
                else:
                    if normal > 0:
                        normal -= 1
                        dirty += 1
                    else:
                        gameover = True
                        break
            if Days[i] == 2:
                if special > 0:
                    special -= 1
                    dirty += 1
                else:
                    gameover = True
                    break
    if amountNeeded + normal > N:
        amountNeeded -= 1
        break
    if gameover != True:
        break
    else:
        amountNeeded += 1
print(amountNeeded)



         