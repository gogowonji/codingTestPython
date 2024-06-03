def solution(s):
    answer = True
    temp = []
    
    for i in s:
        if i == '(':
            temp.append('(')
        if i == ')' and len(temp) != 0:
                temp.pop()
        elif i == ')' and len(temp) == 0:
                return False
                
        
    
    # if len(temp) != 0:
    #     answer = False
    
    return len(temp) == 0