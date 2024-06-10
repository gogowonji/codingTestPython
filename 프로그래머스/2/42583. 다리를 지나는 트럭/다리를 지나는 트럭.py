from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    curWeight = 0
    time = 0
    print(f"bridge : {bridge}")
    while bridge:
            time += 1
            curWeight -= bridge.popleft()
            
            if trucks:
                if curWeight + trucks[0] <= weight:
                    truck = trucks.popleft()
                    bridge.append(truck)
                    curWeight += truck
                else:
                    bridge.append(0)
            
            
            
    return time

# 개수와 무게 제한을 어디에 해야 할까..
# len(temp) <= length and temp 총 값 <= weight
# 제한 걸고 temp push, truck_weights에서 pop
# pop 여러번 해야 하는 경우 - 제한 ㄱㅊ으면 루프 돌게
# 루프 몇번 도는지 셀때 answer++
# 트럭 pop도 해주면서 answer++?
# if len(temp) <= bridge_length and sum(temp) <= weight:
            #     for t in range(len(truck_weights)):
            #         temp.append(truck_weights.pop(0))
            # temp.pop(0)

# deque 학습 필요

