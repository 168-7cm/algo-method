# 標準入力
N, X, Y = map(int, input().split())

dp = [None] * N

# 0番目はX、１番目はYの値
dp[0], dp[1] = X, Y

for i in range(2, N):
    dp[i] = (dp[i-1] + dp[i-2]) % 100

print(dp[N-1])
