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