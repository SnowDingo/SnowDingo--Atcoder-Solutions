# -*- coding: utf-8 -*-
N = int(input())
Ds = list(input().split())
for i in range(0,len(Ds)):
    Ds[i] = int(Ds[i])
totalDays = sum(Ds)
days = 0
daysArray = []
for i in range(0,N):
    for x in range(0,Ds[i]+1):
            if len(str(i+1)) >= 2:
                 if str(i+1)[0] != str(i+1)[1]:
                      break
            if len(str(x)) >= 2 and str(x) == str(i+1):
                days += 1
                daysArray.append(str(i+1) + str(x))
                continue
            elif len(str(x)) < 2 and str(x) == str(i+1):
                days += 1
                daysArray.append(str(i+1) + str(x))
                continue
            elif len(str(x)) >= 2:
                correct = False
                for z in range(0,len(str(x))):
                    if str(x)[z] == str(i+1):
                          continue
                    else:
                        break
                else:
                    days += 1
                    daysArray.append(str(i+1) + str(x))
                    continue
            elif len(str(x)) < 2:
                 if str(x) in str(i+1):
                      days += 1
                      daysArray.append(str(i+1) + str(x))
                      continue
print(days)