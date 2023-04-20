import sys
input=sys.stdin.readline

#############경로의 최댓값은 1억인 걸로 하자.

INF=100000000

num_Node=int(input())
cost=[[0 for _ in range(num_Node)] for i in range(num_Node)]
for i in range(num_Node):
    cost[i]=list(map(int, input().split()))