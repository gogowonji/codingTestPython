# 도화지의 크기를 정의합니다.
DOHWAJI_SIZE = 100

# 도화지를 2D 배열로 초기화합니다.
dohwaji = [[0] * DOHWAJI_SIZE for _ in range(DOHWAJI_SIZE)]

# 색종이의 수를 입력받습니다.
n = int(input())

# 색종이 위치를 입력받아 도화지에 붙입니다.
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            dohwaji[i][j] = 1

# 검은 영역의 넓이를 계산합니다.
black_area = sum(sum(row) for row in dohwaji)

print(black_area)
