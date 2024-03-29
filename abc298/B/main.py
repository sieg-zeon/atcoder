#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def rotate(a):
  n = len(a)
  res = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      res[j][n-1-i] = a[i][j]
  return res

def solve(N: int, A: "List[List[int]]", B: "List[List[int]]"):
  for _ in range(4):
    can = True
    for i in range(N):
      for j in range(N):
        if A[i][j] == 1 and B[i][j] == 0:
          can = False
    if can:
      print("Yes")
      break
    # 90度回転はこうするらしい
    # A = list(map(list, zip(*A[::-1])))
    A = rotate(A)
  else:
    print("No")

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
  def iterate_tokens():
    for line in sys.stdin:
      for word in line.split():
        yield word
  tokens = iterate_tokens()
  N = int(next(tokens))  # type: int
  A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
  B = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
  solve(N, A, B)

if __name__ == '__main__':
  main()
