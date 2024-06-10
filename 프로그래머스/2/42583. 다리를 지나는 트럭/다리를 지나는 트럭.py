from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    curWeight = 0
    time = 0
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
# -> 다리에 올라가는 트럭이 모두 사라질때까지..! if문으로

# if len(temp) <= bridge_length and sum(temp) <= weight:
# -> 다리에 올라가는 트럭 deque를 따로 만들기 and 현재 무게를 계산하도록 변수 생성 후 if문

# 제한 걸고 temp push, truck_weights에서 pop
# pop 여러번 해야 하는 경우 - 제한 ㄱㅊ으면 루프 돌게
# -> 여러번 해야 하는 경우 x <- 시간마다 pop하는 거니까 트럭을 다리에 올리기 전 다리 올라간 트럭들 pop해주면 되는 거였음

# 루프 몇번 도는지 셀때 answer++
# 트럭 pop도 해주면서 answer++?
# -> 1대 이상 있고, 이미 무게를 초과한 경우
# -> bridge.append(0)로 무게 초과한 경우에도 대수 제한 유지 + 시간은 제대로 흐를 수 있게


# POINT
# deque
# 다리 위에 올라가는 트럭 deque
# 대기 중인 트럭 deque
# 현재 무게 저장 변수
# 무게 초과시, 다리 위에 올라가는 트럭 deque에 0 push하기

