# -*- coding: utf-8 -*-
M, D = map(int,input().split())
y,m,d = map(int,input().split())
if m != M and d != D:
    print(str(y) + " " + str(m) + " "  + str(d + 1))
elif m!=M and d == D:
    print(str(y) + " " + str(m + 1) + " "  + str(1))
elif m==M and d != D:
    print(str(y) + " " + str(m) + " "  + str(d+1))
else:
    print(str(y+1) + " " + str(1) + " " + str(1))