def solution(clothes):
    answer = 1
    dic = {}
    for d,t in clothes:
        if t in dic.keys():
            dic[t] += [d]
        else:
            dic[t] = [d]
    
    for _, v in dic.items():
        answer *= (len(v)+1)
        
    
    return answer - 1