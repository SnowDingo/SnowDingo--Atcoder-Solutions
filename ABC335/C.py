# -*- coding: utf-8 -*-
from collections import deque
N, Q = map(int,input().split())
Command = []
Points = deque()
for i in range(0,Q):
    Command.append(input().split())
for i in range(0,N):
    Points.append([i+1,0])
## ここで命令を実行する
for i in range(0,Q):
    if Command[i][0] == "1":
        if Command[i][1] == "R":
            for i in range(0,len(Points)):
                if i <= 1:
                    Points.pop()
                    Points.append(Points[0])
                else:
                    Points.append([Points[i][0]+1,Points[i][1]])
        if Command[i][1] == "L":
            for i in range(0,len(Points)):
                if i <= 1:
                    Points.pop()
                    Points.append(Points[0])
                else:
                    Points.append([Points[i][0]-1,Points[i][1]])
        if Command[i][1] == "U":
             for i in range(0,len(Points)):
                if i <= 1:
                    Points.pop()
                    Points.append(Points[0])
                else:
                    Points.append([Points[i][1]+1,Points[i][1]])
        if Command[i][1] == "D":
             for i in range(0,len(Points)):
                if i <= 1:
                    Points.pop()
                    Points.append(Points[0])
                else:
                    Points.append([Points[i][1]-1,Points[i][1]])
    elif Command[i][0] == "2":
        print(str((Points[(int(Command[i][1])-1)])))
        #print(Points)
        continue