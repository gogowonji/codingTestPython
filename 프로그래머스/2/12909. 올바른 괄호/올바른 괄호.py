# if문 return문 배우기
# 예외처리 왜 안되는지 모르겠다
# try:
#    temp.pop()
# except IndexError:
#    return False

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
    return len(temp) == 0
