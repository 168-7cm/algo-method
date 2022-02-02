# 標準入力
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 3×Nの多次元配列を作成する
dp = [[None] * 3 for _ in range(N)]

# 0日目の情報をセットする
for i in range(3):
    dp[0][i] = A[0][i]

# 動的計画法
for i in range(1, N):
    # i日目の仕事0の報酬 = i-1日目の仕事1,2の最大値 + i日目の仕事0の報酬
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + A[i][0]
    # i日目の仕事1の報酬 = i-1日目の仕事0,2の最大値 + i日目の仕事1の報酬
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + A[i][1]
    # i日目の仕事2の報酬 = i-1日目の仕事0,1の最大値 + i日目の仕事2の報酬
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + A[i][2]

print(max(dp[N-1]))
