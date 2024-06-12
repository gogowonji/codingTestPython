# 정렬 문제라고 하니까..
# 정렬 후 중앙값 찾기
# 정렬 - 시간 복잡도..
# index
# 홀수개 len/2 + 1
# 짝수개 len/2
# answer = 0
# index = 0
# citations.sort()
# print(citations)
# index = (int)(len(citations)/2)
# answer = citations[index]
# return answer
def solution(citations):
    answer = 0
    
    hIndex = []
    citations.sort()
    
    for c in range(len(citations)):
        count = 0
        for i in range(len(citations)):
            if citations[c] <= citations[i]:
                count += 1
        hIndex.append(min(count,citations[c]))
        
    print(hIndex)
    answer = max(hIndex)
    return answer;
    
