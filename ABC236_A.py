import io
import sys

_INPUT = """\
6
chokudai
3 5
aa
1 2
aaaabbbb
1 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=list(input())
  a,b=map(int,input().split())
  S[a-1],S[b-1] = S[b-1],S[a-1]
  print(*S,sep='')