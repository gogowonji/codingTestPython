# 입출력 예 설명
# 1초의 주가는 1이며 1초부터 5초까지 총 4초간 주가를 유지했습니다.
# 2초의 주가는 2이며 2초부터 5초까지 총 3초간 주가를 유지했습니다.
# 3초의 주가는 3이며 4초의 주가는 2로 주가가 떨어졌지만 3초에서 4초가 되기 직전까지의 1초간 주가가 유지 된것으로 봅니다. 따라서 5초까지 총 1초간 주가를 유지했습니다.
# 4초의 주가는 2이며 4초부터 5초까지 총 1초간 주가를 유지했습니다.
# 5초의 주가는 3이며 5초 이후로는 데이터가 없으므로 총 0초간 주가를 유지했습니다.

from collections import deque
def solution(prices):
    que = deque(prices)
    answer = []
    
    while que:
        price = que.popleft()
        sec = 0
        for p in que:
            sec += 1
            if price > p:
                break;
        answer.append(sec)
            
        
    return answer
# 뒤 항목 비교하면서 뒤 값이 크면 +1
# 본인 < 비교값 (주가 유지) +1
# 그렇지 않을 경우 continue
# -> continue가 아니라 break 되야... 이후 시간은 무시해야 함 (문제 이해 잘못했네~)

# for p in range(len(prices)):
#     sec = 0
#     for i in range(p+1,len(prices)):
#         if prices[p] <= prices[i]:
        # -> 이후 시간은 무시해야 하는 걸 몰랐다 (문제 이해 잘못)
#             sec += 1
#     answer[p].append(sec)
        # -> answer[p].append(sec)은 잘못 되었다... answer이 빈 리스트이기 때문에 append()로 추가해야 함

# 내가 생각했던 풀이 -> 수정 완료
# def solution(prices):
    
#     answer = []
    
#     for p in range(len(prices)):
#         sec = 0
#         for i in range(p+1,len(prices)):
#             sec += 1
#             if prices[p] > prices[i]:
#                 break
#         answer.append(sec)
                    
#     return answer
