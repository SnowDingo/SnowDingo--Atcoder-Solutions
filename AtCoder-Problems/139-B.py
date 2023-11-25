# -*- coding: utf-8 -*-
A, B = map(int, input().split())
plugs = 0
goal = B - 1
while A * plugs < B:
    plugs += 1
print(plugs)
