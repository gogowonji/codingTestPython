# ord()
# enumerate(), 리스트컴프리헨션
# 여러번 세어진 것을 구하는 부분이 헷갈렸음

# print(ord('a'))  #97
# print(ord('A'))  #65
# print(ord('z')) #122
# print(ord('Z')) #90


s = str(input())
answer = ''
count = [0] * 26
max_count = 0

for i in s:
  if (ord(i) >= ord('a')):  #소문자이면
    count[ord(i) - ord('a')] += 1
    
  else:  #대문자이면
    count[ord(i) - ord('A')] += 1
    

# 여러번 세어진 것을 구함
max_answer = 0
max_count = max(count)
max_answer = [i for i,v in enumerate(count) if v == max_count]

if len(max_answer) > 1:# 여러번 세어진 것을 구함
    print('?')
else:
  answer = chr(max_answer[0] + ord('A'))
  print(answer)
