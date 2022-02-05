import io
import sys

_INPUT = """\
6
3
1 3 2 3 3 2 2 1 1 1 2
1
1 1 1
4
3 2 1 1 2 4 4 4 4 3 1 3 2 1 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  x=[0]*N
  for i in range(4*N-1):
    x[A[i]-1]+=1
  for i in range(N):
    if x[i]==3:
      print(i+1)