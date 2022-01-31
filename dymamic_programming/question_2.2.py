# 標準入力
N = int(input())
A = list(map(int, input().split()))

dp = [[None] * N for _ in range(N)]

# 0列目の値は、A[i]の値と同じ
dp[0] = A

# 動的計画法
for i in range(1, N):
    for j in range(0, N):
        if j == 0:
            # 1番左の場合：
            dp[i][j] = (dp[i-1][j] + dp[i-1][j+1]) % 100
        elif j == N-1:
            # 1番右の場合
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 100
        else:
            # それ以外の場合
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]) % 100

print(dp[N-1][N-1])
