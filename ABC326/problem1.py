# -*- coding: utf-8 -*-
X,T = map(int,input().split())
if X > T and X-T <= 3:
    print("Yes")
elif X>T and not X-T <= 3 :
    print("No")
elif X<T and  T-X <= 2:
    print("Yes")
elif X<T and  not T-X <= 2:
    print("No")