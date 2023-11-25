# -*- coding: utf-8 -*-
#NはSのながさ
N = int(input())
#Sは文字列
S = str(input())
#全てのけたと同じか確認するプログラム
def alltrue(n):
    count = 0
    for i in range(0,n):
        if S[i] == S[n]:
            count +=1
    if count == N:
        return True
    else:
        return False
#コードテンプレ
already = []
count = 0
for i in range(0,N):
    while True:
        rangenum = i+1
        if S[i] not in already:
                count += 1
                already.append(S[i])
                while True:
                    print(S[i:rangenum])
                    if alltrue(rangenum) and  S[i:rangenum] not in already:
                        count += 1
                        rangenum += 1
                        already.append[S[i:i+rangenum]]
                    else:
                        break
        else:
            break
print(already)
print(count)