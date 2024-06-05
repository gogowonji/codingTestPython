def solution(priorities, location):
    answer = 0
    que = [(i,p) for i, p in enumerate(priorities)]
    
    while True:
        pro = que.pop(0)
        if any(pro[1] < q[1] for q in que):
            que.append(pro)
        else:
            answer += 1
            if(pro[0] == location):
                return answer
    
# 큐에서 빼고
# 큐에서 빼낸 값보다 작은 값 있는지 => 크기 비교를 어떻게 하지? & 인덱스값 해당하는 애 어떻게?
# 실행
# 없으면 다시 넣고 종료
#     que = []
#     for p, i in zip(priorities, range(len(priorities))):
#         que.append((i,p))
#     # 튜플 까지는 접근 했는데 ㅠ
    
#     while len(que) > 0:
#         tmp = que.pop(0)
#         for p in que:
            
#             if tmp < p: #크면 뒤로 보내야
#                 priorities.append(tmp)
#             else:
#                 if(tmp == )
