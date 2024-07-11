# 1940 주몽
# 입력
# 6
# 9
# 2 7 4 1 5 3
# -> 1 2 3 4 5 7
# 2,7 4,5
# 출력
# 2

def search(arr, start, target):
    end = len(arr)-1
    val = target - arr[start]
    for i in range(1,len(arr) - start):
        if arr[start+i] == val:
            return 1
    return 0


N = int(input())
M = int(input())
numbers = list((map(int, input().split())))

# M이 될ㄸㅐ 까지 탐색하는거 -> 이분 탐색으로?
count = 0
numbers.sort()
for i in range(N):
    count += search(numbers,i,M)
print(count)


