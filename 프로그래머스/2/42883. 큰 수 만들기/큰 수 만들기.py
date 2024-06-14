# 그리디니까 제일 작은 값이랑 순서대로 작은 값 찾을까?
# -> 그리디여서 큰 값을 찾아야 함
# -> 큰 값을 찾아서 그것을 스택(순서가 정해져 있으니까) 만드는 방법을 생각해야 함
# ** stack[-1] : 마지막 값인데 -1을 설정하면 stack이 비어있어도 할 수 있으니까..
# ** -> stack 조건 추가


# return 값이 제거가 끝난 후 남는 가장 큰 수
# ** pop()
# -> 그냥 값을 삭제하는 거지, 인덱스나 값으로 삭제하는 게 아님
 
def solution(number, k):
    stack = []
    for num in number:
        # 현재 숫자가 stack의 마지막 숫자보다 크고, 제거할 k의 횟수가 남아있을 때
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 k가 남아있는 경우, 뒤에서부터 k개를 제거
    # -> 남아 있을 경우 정렬되어 있는 경우라고 볼 수 있어서
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
