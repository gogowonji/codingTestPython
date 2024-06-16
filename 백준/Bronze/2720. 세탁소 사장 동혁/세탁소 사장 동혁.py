coin_types = [25,10,5,1]

T = int(input())
for _ in range(T):
    money = int(input())
    answer = []
    for coin in coin_types:
        answer.append(money//coin)
        money %= coin
    print(*answer)
