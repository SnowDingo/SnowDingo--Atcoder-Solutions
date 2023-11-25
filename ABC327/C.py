# -*- coding: utf-8 -*-
data = []
data = [input().split() for i in range(9)]  
#最初の数値が縦、次が横
for i in range(0,8):
    reserved = []
    for x in range(0,8):
        if data[i][x] in reserved:
            print("No")
            exit()
        else:
            reserved.append(data[i][x])
for i in range(0,8):
    reserved = []
    for x in range(0,8):
        if data[x][i] in reserved:
            print("No")
            exit()
        else:
            reserved.append(data[x][i])
for x0 in range(0,7,3):
    for y0 in range(0,7,3):
        reserved = []
        for dx in range(0,3):
            for dy in range(0,3):
                if data[x0+dx][y0+dy] in reserved:
                    print("No")
                    exit()
                else:
                    reserved.append(data[x0+dx][y0+dy])
print("Yes")
exit()