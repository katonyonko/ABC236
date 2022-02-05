import io
import sys

_INPUT = """\
6
5 3
tokyo kanda akiba okachi ueno
tokyo akiba ueno
7 7
a t c o d e r
a t c o d e r
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  S=list(input().split())
  T=list(input().split())
  d=dict()
  d2=dict()
  for i in range(N):
    d[i]=S[i]
    d2[S[i]]=i
  for i in range(M):
    d[d2[T[i]]]=-1
  for i in range(N):
    if d[i]==-1:
      print('Yes')
    else:
      print('No')