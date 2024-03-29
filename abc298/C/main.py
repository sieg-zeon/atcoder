#!/usr/bin/env python3
import bisect,collections,copy,heapq,itertools,math,string,queue
import sys
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def S(): return input()
def MS(): return input().split()
def LS(): return list(input().split())




# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
  N = I()
  Q = I()
  boxes = [[] for _ in range(N)]
  cards = [[] for _ in range(200001)]
  for _ in range(Q):
    query = LI()
    q = query[0]
    i = query[1]
    if q == 1:
      j = query[2]
      boxes[j-1].append(i)
      if not j in cards[i-1]:
        cards[i-1].append(j)
    elif q == 2:
      print(*sorted(boxes[i-1]))
    else:
      print(*sorted(cards[i-1]))


if __name__ == '__main__':
  main()
