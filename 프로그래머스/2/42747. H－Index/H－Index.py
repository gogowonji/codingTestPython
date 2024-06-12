# h-index 개념이 이해가 안됐음 -> 리트코드 참고

# 정렬 후 중앙값 찾기
# -> 중앙값을 찾는 문제인줄 알았음 (아니었음)
# 정렬 - 시간 복잡도..
# index
# 홀수개 len/2 + 1
# 짝수개 len/2

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
    
