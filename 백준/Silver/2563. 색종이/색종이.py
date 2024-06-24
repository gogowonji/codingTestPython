# 좌표 영역 2차원 배열로 받아오는 아이디어!
# 겹쳐진 영역, 안 겹쳐진 영역 상관 없이 1 넣기
# 행마다 sum하기

# 도화지 크기
DOHWAJI_SIZE = 100
# 좌표 영역을 2차원 배열로 저장
dohwaji = [[0] * DOHWAJI_SIZE for _ in range(DOHWAJI_SIZE)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            dohwaji[i][j] = 1

# 검은 영역 줄마다..
black_area = sum(sum(row) for row in dohwaji)

print(black_area)
