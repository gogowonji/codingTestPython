import math
def solution(progresses, speeds):
    answer = []
    
    days = 0
    count = 0
    # 시간에 따라 progresses을 증가시킴
    while len(progresses) > 0:
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            else: # 아무조건에 해당하지 않으면 다음날 이동
                days += 1
    answer.append(count)
    return answer