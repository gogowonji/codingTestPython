def solution(s):
    answer = True
    temp = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    for i in s:
        if i == '(':
            temp.append('(')
        elif i == ')' and len(temp) != 0:
            temp.pop()
        elif i == ')' and len(temp) == 0:
            return False
        
    
    if len(temp) != 0:
        answer = False
    
    return answer