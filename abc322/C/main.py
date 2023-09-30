#!/usr/bin/env python3
import collections
import sys


def solve(N: int, M: int, A: "List[int]"):
  q = collections.deque(A)
  for i in range(1, N + 1):
    t = q[0]
    if i <= t:
      print(t-i)
    else:
      q.popleft()
      t = q[0]
      print(t-i)
  return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
  def iterate_tokens():
    for line in sys.stdin:
      for word in line.split():
        yield word
  tokens = iterate_tokens()
  N = int(next(tokens))  # type: int
  M = int(next(tokens))  # type: int
  A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
  solve(N, M, A)

if __name__ == '__main__':
  main()
