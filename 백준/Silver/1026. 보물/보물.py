# sorted(list(map(int,input().split())),reserve=True)
# -> 바로 작성할 수 있었음

A = []
B = []
result = 0
N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort(reverse=True)
B.sort()
for i in range(N):
  result += A[i]*B[i]

print(result)
