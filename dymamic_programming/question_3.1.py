
# 標準入力
N, M = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j] マス(i,j)にコマが存在するかどうか
dp = [[0] * M for _ in range(N)]

dp[0][0] = True

for i in range(N-1):
    for j in range(M):

        # マス (i, j) にコマがいく可能性がない場合はスキップ
        if not dp[i][j]:
            continue

        # 真下マスへコマを渡す
        dp[i+1][j] = True

        # 右下マスへコマを渡す
        if j+A[i] < M:
            dp[i+1][j+A[i]] = True

# 集計する
print(sum(dp[N-1]))
