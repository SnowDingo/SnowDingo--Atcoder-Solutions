# -*- coding: utf-8 -*-
N,a,b=(int(x) for x in input().split())
numbers = []
for i in range(1,N+1):
  digitslist = list(map(int, str(i)))
  digit = sum(digitslist)
  if digit >= a and digit <= b:
    numbers.append(i)
    continue
  else:
    continue
print(sum(numbers))