# 標準入力
N = int(input())
A = list(map(int, input().split()))

# 0マス目からNマス目までの配列
dp = [None] * N

# 0マス目→0
dp[0] = 0

for i in range(1, N):
    if i == 1:
        dp[i] = dp[0] + A[i]
    else:
        dp[i] = min(dp[i-1] + A[i], dp[i-2] + 2 * A[i])

print(dp[N-1])
