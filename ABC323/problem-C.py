# -*- coding: utf-8 -*-
N, M = map(int,input().split())
ProblemPoints = list(input().split())
PointsSorted = sorted(ProblemPoints,reverse=True)
Results = {}
for i in range(0,N):
    teamscore = input()
    Results[i+1] = str(teamscore)

points = {}
for i in range(1,N+1):
    point = 0
    for s in range(0,len(Results[i])):
        if Results[i][s] == "o":
            point += int(ProblemPoints[s])
            continue
        else:
            continue
    points[i] = point
print(points)
for i in range(1,N):
    if max(dict(points).values()) == points[i]:
        print(0)
    else:
        problemsneed = 0
        extrapointsneed = 0
        for x in range(0, len(PointsSorted)):
            points[i] = tuple(PointsSorted[x])
            if  max(dict(points).values()) < points[i] :
                problemsneed = x
                break
        print(problemsneed)