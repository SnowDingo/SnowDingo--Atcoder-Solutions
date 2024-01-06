N,Q=map(int,input().split())
A=[(i+1,0) for i in range(N)][::-1]
for _ in range(Q):
  T,C=input().split()
  if T=="1":
    x,y=A[-1]
    if C=="U": y+=1
    if C=="D": y-=1
    if C=="R": x+=1
    if C=="L": x-=1
    A.append((x,y))
  else:
    print(*A[-int(C)])
