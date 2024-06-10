# 최대로 다른 종류 수 구하기
def solution(nums):
    answer = 0
    count = len(set(nums))
    sel = len(nums)/2
    if count < sel:
        answer = count
    else :
        answer = sel
    return answer

    