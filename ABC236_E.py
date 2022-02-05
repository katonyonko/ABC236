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
  l,r=0,max(A)
  for i in range(40):
    tmp=(l+r)/2
    s=0
    a=0
    for j in range(N):
      if A[j]>=tmp:
        a+=A[j]-tmp
      else:
        if s==0:
          if j<N-1:
            a+=max(A[j],A[j+1])-tmp
          s=1
        else:
          s=0
    if a>=0:
      l=tmp
    else:
      r=tmp
  print(l)