# 1940 주몽
# 선형 탐색

def search(arr, start, target):
    end = len(arr) - start
    val = target - arr[start] # M의 값이 되도록
    for i in range(1,end):
        if arr[start+i] == val: # 두 값의 합 == M의 값 일 때
            return 1
    return 0


N = int(input())
M = int(input())
numbers = list((map(int, input().split())))

count = 0
numbers.sort()
for i in range(N):
    count += search(numbers,i,M)
print(count)


