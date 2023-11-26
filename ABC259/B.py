# -*- coding: utf-8 -*-
import math
a,b,d = map(int,input().split())
d = math.radians(d)
x =  a*math.cos(d) - math.sin(d) * b
y  =  a * math.sin(d) + math.cos(d) * b
print(str(x) + " " + str(y))