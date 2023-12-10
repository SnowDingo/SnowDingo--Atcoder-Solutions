# -*- coding: utf-8 -*-
N = int(input())
As = list(map(int,input().split()))
answer = ""
def compare(list,index):
    value = 0
    for i in list:
        if list[index] < i:
            value += i
    return value

for i in range(0,N):
    answer = answer + str((compare(As,i))) + " "
print(answer)