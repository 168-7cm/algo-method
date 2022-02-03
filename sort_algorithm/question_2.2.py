# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

# 並び替え
A.sort()

for i in range(M):
    print(A[X[i]])
