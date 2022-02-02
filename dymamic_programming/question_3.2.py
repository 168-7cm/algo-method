# 標準入力
# N個のボール、Mグラムまで
N, M = map(int, input().split())
W = list(map(int, input().split()))

# dp[i][j] i個のボール使ってjグラムを満たすかどうか
dp = [[0] * (M+1) for _ in range(N+1)]

# 0個のボールで、0グラムはできる
dp[0][0] = True

# 0個のボールで、1〜Mグラムはできない
for i in range(1, M+1):
    dp[0][i] = False

# 1以降で動的計画法
for i in range(1, N+1):
    for j in range(0, M+1):
        if j < W[i-1]:
            # Jグラムにしたいため、ボールの重さ（W[i-1]）がJより大きい場合は選択できない。
            dp[i][j] = dp[i-1][j]
        else:
            if (dp[i-1][j] or dp[i-1][j-W[i-1]]):
                # ①ボール[i-1]までの総和が、jであり、ボール[i]を選択しない or ②ボール[i-1]までの総和が、j-W[i]であり、ボール[i]を選択する。
                dp[i][j] = True
            else:
                dp[i][j] = False
print('Yes' if dp[N][M] else 'No')
