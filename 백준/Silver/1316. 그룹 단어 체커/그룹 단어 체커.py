answer = 0

N = int(input())

for _ in range(N):
  abc = [False] * 26
  isGroup = True
  word = str(input())
  abc[ord(word[0]) - 97] = True
  for i in range(1, len(word)):
    if word[i - 1] != word[i]:
      if abc[ord(word[i]) - 97]:
        isGroup = False
        break
      abc[ord(word[i]) - 97] = True

  if isGroup:
    answer += 1

print(answer)
