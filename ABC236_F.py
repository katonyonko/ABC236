import io
import sys

_INPUT = """\
6
2
4 5 3
4
9 7 9 7 10 4 3 9 4 8 10 5 6 3 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def ld(x):
    return x&(-x)
  N=int(input())
  c=list(map(int,input().split()))
  tmp=[(c[i],i+1) for i in range(2**N-1)]
  tmp.sort()
  ans=0
  l=[]
  for i in range(2**N-1):
    C,T=tmp[i]
    for j in range(len(l)):
      if T&l[j][0]!=0: T^=l[j][1]
    if T!=0:
      ans+=C
      l.append((ld(T),T))
  print(ans)