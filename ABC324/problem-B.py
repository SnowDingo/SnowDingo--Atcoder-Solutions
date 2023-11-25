# -*- coding: utf-8 -*-
import math
from collections import Counter
N = int(input())
M = N/2
# 素因数分解を行う関数
    # Counterクラスを呼び出してオブジェクト生成
counter = Counter()
    
    # 素数で割り切れるかの判定
for p in range(2, int(N ** 0.5) + 1):
        # １回割り切れるごとに+1カウントしていく
        while N % p == 0:
            counter[p] += 1
            N //= p
    # n が1より大きい数字として残っていれば、素数
        if N != 1:
            counter[N] += 1
wow = 0
result = counter
arraay = list(counter.keys())
for i in range(0,len(arraay)):
     if arraay[i] %2 == 0 or arraay[i] % 3 == 0:
          continue
     else:
          print("No")
          exit()
print("Yes")