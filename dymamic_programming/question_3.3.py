# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# N × M のマスを用意する
# 配列全体を -1 で初期化する
# 計算終了後に -1 であるマスは、到達不能であることを表す
dp = [[-1] * M for _ in range(N)]

# 初期状態
# 左上のマスにいるとき、スコアは 0
dp[0][0] = 0

# 各マス (i, j) から「真下」「右下」へコマを渡していく
for i in range(N-1):
    for j in range(M):

        # マス (i, j) にコマがいく可能性がない場合はスキップ
        if dp[i][j] < 0:
            print(i, j)
            continue

        # 真下マスへコマを渡す (スコアは変化なし)
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        # 右下マスへコマを渡す (スコア B[i] を加算)
        if j+A[i] < M:
            dp[i+1][j+A[i]] = max(dp[i+1][j+A[i]], dp[i][j] + B[i])

# 答え
print(dp[N-1][M-1])
