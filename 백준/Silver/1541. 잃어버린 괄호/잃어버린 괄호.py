# 마이너스(-) 사이 값들을 괄호처리해주면 된다는 그리디 아이디어
# split()을 잘 활용해서 풀어야 하는 문제
# 저장된 처음 값은 뺄 수 없기 때문에 answer에 미리 저장해주기

question = str(input()).split('-')

list = []
for q in question:
  sum = 0
  for val in q.split('+'):
    sum += int(val)
  list.append(sum)

answer = list[0]
for v in list[1:]:
  answer -= v
print(answer)
