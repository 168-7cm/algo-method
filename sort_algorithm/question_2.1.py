# 入力
N = int(input())
A = list(map(int, input().split()))

# 並び替え
A.sort()

center = 0

if N % 2 == 0:
    # 偶数
    center = (A[N // 2 - 1] + A[N // 2]) / 2
else:
    # 奇数
    # 「//」は切り捨て除算なので、N-1にしなくても同じ
    center = A[N // 2]

print(center)
