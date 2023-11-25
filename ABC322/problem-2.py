# -*- coding: utf-8 -*-
N, M = int, input().split()
S = str(input())
T = str(input())

if T.startswith(S) and T.endswith(S):
    print(0)
elif T.startswith(S) and not T.endswith(S):
    print(1)
elif not T.startswith(S) and  T.endswith(S):
    print(2)
else:
    print(3)