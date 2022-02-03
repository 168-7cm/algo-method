# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 並び替え
A.sort(reverse=True)

# 合計
sum = 0

for i in range(K):
    sum += A[i]

print(sum)
