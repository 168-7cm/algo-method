# 標準入力
N = int(input())


def isPrime(N):
    # 0,1は素数でない
    if N < 2:
        return False
    # 1とN以下の整数で割れるか確認→割れる場合あまりが0
    for i in range(2, N):
        if N % i == 0:
            return False
    return True


print("Yes" if isPrime(N) else 'No')
