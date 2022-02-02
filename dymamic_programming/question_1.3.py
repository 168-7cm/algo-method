# 標準入力
N = int(input())

# 0〜N段目までのパターンの配列
dp = [None] * (N + 1)

# 0段目にいく方法は1パターン
dp[0] = 1

for i in range(1, N + 1):
    if i == 1:
        dp[i] = dp[0]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
