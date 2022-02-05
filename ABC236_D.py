import io
import sys

_INPUT = """\
6
2
4 0 1
5 3
2
1
5
5
900606388 317329110 665451442 1045743214 260775845 726039763 57365372 741277060 944347467
369646735 642395945 599952146 86221147 523579390 591944369 911198494 695097136
138172503 571268336 111747377 595746631 934427285 840101927 757856472
655483844 580613112 445614713 607825444 252585196 725229185
827291247 105489451 58628521 1032791417 152042357
919691140 703307785 100772330 370415195
666350287 691977663 987658020
1039679956 218233643
70938785
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=[list(map(int,input().split())) for _ in range(2*N-1)]
  tmp=list(range(2*N))
  t=0
  ans=-1
  def rec(x):
    global t
    global ans
    if len(x)==0: ans=max(ans,t)
    for i in range(len(x)-1):
      t=t^A[x[0]][x[i+1]-x[0]-1]
      rec([x[j] for j in range(len(x)) if j!=0 and j!=i+1])
      t=t^A[x[0]][x[i+1]-x[0]-1]
  rec(tmp)
  print(ans)