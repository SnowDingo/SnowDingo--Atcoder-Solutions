# -*- coding: utf-8 -*-

N, X = map(int, input().split())
As = [int(x) for x in input().split()]

As = sorted(As)
for x in range(0,101):
    scorenow = As[0:len(As)]
    scorenow.append(x)
    scorenow.remove(max(scorenow))
    scorenow.remove(min(scorenow))
    if sum(scorenow) >= X:
        print(x)
        exit()
    else:
        continue
print(-1)