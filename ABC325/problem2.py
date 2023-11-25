# -*- coding: utf-8 -*-
N = int(input())
WX = []
for i in range(0,N):
    W,X = map(int, input().split())
    WX.append((W,X))
availableperson = []
max = []
TimeNow = []
Persons = []
people = []
for time in range (0,25):
    availableperson = []
    TimeNow = []
    Persons = []
    for i in range(0,int(len(WX))):
        Wi,Xi = WX[i]
        if Xi + time < 24:
            TimeNow.append(Xi+time)
        else:
            TimeNow.append(Xi +time - 24)
        Persons.append(Wi)
    for x in range(0,len(TimeNow)):
        if TimeNow[x] <= 9 or TimeNow[x] >= 18:
            continue
        else:
            availableperson.append(Persons[x])
            continue
    people.append(sum(availableperson))
print(sorted(people,reverse=True)[0])
