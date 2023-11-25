# -*- coding: utf-8 -*-
N = int(input())
Results = {}

for i in range(0,N):
    teamscore = input()
    Results[i+1] = str(teamscore)
wins = {}
for i in range(1,N+1):
    win = 0
    for s in range(0,len(Results[i])):
        if Results[i][s] == "o":
            win += 1
            continue
        else:
            continue
    wins[i] = win

wins = sorted(wins.items(), key=lambda x:x[1], reverse=True)
final = ""
for i in dict(wins).keys():
    final = final + str(i) + " "
print(final)