# 入力
N = int(input())
A = list(map(int, input().split()))

# 選択ソート
for i in range(0, N-1):
    min_position = i
    min_value = A[i]
    flug = False
    for j in range(i+1, N):
        if A[j] < A[min_position]:
            min_position = j
            min_value = A[j]
            flug = True
    A[i], A[min_position] = A[min_position], A[i]

    if flug:
        print(A)
