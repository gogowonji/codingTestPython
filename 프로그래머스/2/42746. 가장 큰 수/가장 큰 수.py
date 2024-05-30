def solution(numbers):
    strNum = sorted(list(map(str,numbers)), reverse=True, key= lambda x:x*3)
    answer = ''.join(strNum)
    return str(int(answer))