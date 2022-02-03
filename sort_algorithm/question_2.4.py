# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 並び替え
A.sort()

# 差を初期化する
diff = 100000

# 「連続する K 個の整数」の最大値と最小値の差を求めていく
for i in range(N - k + 1):
    diff = A[i + K-1] - A[i]

    # 最小値を更新
    result = min(result, diff)

print(result)
