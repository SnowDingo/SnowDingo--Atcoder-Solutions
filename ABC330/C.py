# -*- coding: utf-8 -*-
import math
D = int(input())
x =0
#１００万の二乗は１兆らしいのでとりあえず最大値設定
max = 1000000
answer = []
y = x
#XがMaxいないで、さらにXがD以下の時
while x<= max and x**2 + y**2 <= D**2 and x <= D:
    y = x
    while y <= x + 3 and y**2 <= D**2 :
            answer.append(abs(x**2+y**2-D))
            if abs(x**2+y**2-D)==0:
                print(0)
                exit()
            y += 1
    x += 1
print(min(answer))