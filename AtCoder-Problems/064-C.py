# -*- coding: utf-8 -*-
N =  int(input())
ratings = list(input().split())
anycolor = []
colors = []
for x  in ratings:
    if x >= 3200:
        anycolor.append(x)
for i in ratings:
    if i <= 399:
        colors.append("Grey")
    elif i >=400 and i <= 799:
        colors.append("Brown")
    elif i >=800 and i <= 1199:
        colors.append("Brown")
    elif i >=1200 and i <= 1599:
        colors.append("LightBlue")
    elif i >=1600 and i <= 1999:
        colors.append("Brown")