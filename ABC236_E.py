import io
import sys

_INPUT = """\
6
6
2 1 2 1 1 10
7
3 1 4 1 5 9 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  l,r=0,max(A)+1
  while r-l>10**-4:
    tmp=(l+r)/2
    dp=[[0]*2 for _ in range(N+1)]
    for j in range(N):
      dp[j+1][0]=max(dp[j])+A[j]-tmp
      dp[j+1][1]=dp[j][0]
    if max(dp[-1])>=0:
      l=tmp
    else:
      r=tmp
  print(l)
  l,r=0,max(A)+1
  while r-l>1:
    tmp=(l+r)//2
    dp=[[0]*2 for _ in range(N+1)]
    for j in range(N):
      dp[j+1][0]=max(dp[j])+(1 if A[j]>=tmp else -1)
      dp[j+1][1]=dp[j][0]
    if max(dp[-1])>0:
      l=tmp
    else:
      r=tmp
  print(l)