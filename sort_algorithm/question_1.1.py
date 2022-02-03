# 入力
N = int(input())
A = list(map(int, input().split()))

# バブルソート (無限ループ回避のため N 回で打ち切る)
for _ in range(N):
    flag = False
    for i in range(N-1):
        if A[i] > A[i+1]:
            flag = True
            A[i], A[i+1] = A[i+1], A[i]
    if flag:
        print(A)
    else:
        break
