# -*- coding: utf-8 -*-
#Len（S）＝N
#NはSのながさ
N = int(input())
#Sは文字列
S = str(input())
Already = []
#最後に出力する数字
count = 0
#範囲
numrange = 1
for i in range(0,N-1):
    numrange = 1
    while True:
        #SのI文字目からスライスしてくる
        print(numrange)
        if S[i] == S[i+1:i+numrange][0] and S[i] == S[i] == S[i+1:i+numrange][1]  and not S[i] + S[i+1:i+numrange] in Already:
            #既に登録されているモノを入れる
            Already.append(S[i] + S[i+1:i+numrange])
            count += 1
            numrange += 1
        elif range == 1 and not S[i] in Already:
            count+=1
            Already.append(S[i])
        else:
            break
print(count)