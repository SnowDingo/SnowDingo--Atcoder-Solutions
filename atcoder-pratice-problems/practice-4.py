# -*- coding: utf-8 -*-
N = int(input())

numbers = input().split()
number = 0

while True:
    for i in numbers:
            if (int(i) % 2) == 0:
                continue
            else:
                print(number)
                exit()
    number += 1
    x = 0
    for i in numbers:
         numbers[x] = int(i)/2
         x += 1


         
