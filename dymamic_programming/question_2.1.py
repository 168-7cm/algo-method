# 標準入力
A = list(map(int, input().split()))

dp = [[None] * 4 for _ in range(4)]

# 0列目の値は、A[i]の値と同じ
dp[0][0], dp[0][1], dp[0][2], dp[0][3] = A[0], A[1], A[2], A[3]
# A[0] = list(map(int, input().split()))

# 動的計画法
for i in range(1, 4):
    for j in range(0, 4):
        if j == 0:
            # 一番左の場合
            dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
        if j == 1 or j == 2:
            # 真ん中の場合
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
        if j == 3:
            # 左の場合
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[3][3])

# 別解 https://algo-method.com/tasks/324/editorial
