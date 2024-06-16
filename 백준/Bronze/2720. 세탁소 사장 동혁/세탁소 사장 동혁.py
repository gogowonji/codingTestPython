# 그리디
# print(*answer)는 answer 리스트의 요소들을 공백으로 구분하여 출력
# 백준은 출력을 해볼 수가 없어서 제출 * 100번 하게 돼

coin_types = [25,10,5,1]

T = int(input())
for _ in range(T):
    money = int(input())
    answer = []
    for coin in coin_types:
        answer.append(money//coin)
        money %= coin
    print(*answer)
