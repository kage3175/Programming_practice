import sys
sys.setrecursionlimit(10**7)
VAL = 0


def algB(n):
  #print("n: ", n)
  if n <= 1 :
    return 1
  else:
    tmp = 0
    t = algB(n // 3)
    for i in range(1, t + 1):
      tmp += 1
    tmp = tmp + algB((2 * n) // 3)
    return tmp
  
print(algB(10000))