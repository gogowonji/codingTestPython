# 10815 숫자 카드
# 이분 탐색?
def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


N = int(input())
orgin = list((map(int, input().split())))
orgin.sort()
#print(orgin)

M = int(input())
# compare 될 애들이 이분 탐색으로 들어가서 검사
compare = list((map(int, input().split())))
#print(compare)
result = []
for c in compare:
    if binarySearch(orgin, c):
        result.append(1)
    else:
        result.append(0)


for r in result:
    print(r, end=' ')
