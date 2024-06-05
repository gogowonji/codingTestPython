import heapq
def solution(scoville, K):
    answer = 0
   
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    # for s in range(len(scoville)): #scoville 값이 계속 변하는데..?!
    #     scoville.sort()
    #     if scoville[s] >= K:
    #         break
    #     else:
    #         scoville.append(scoville[s] + scoville[s+1]*2)
    #         scoville.pop(0) # 앞 두개 제거
    #         scoville.pop(1)
    #         answer += 1
    #         s = 0
    return answer

# 정렬
# for
# 배열의 맨 앞 숫자가 K이상 인지 확인
# 앞 두개 섞어 새로운 음식
# 제거
# 새로운 음식 만드는 갯수만 반환하면 되니까 다른 배열 만들어?


