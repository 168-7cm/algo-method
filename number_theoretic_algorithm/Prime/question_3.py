def isPrime(N):
    # 0,1は素数でない
    if N < 2:
        return False

    # √Nまで確認すればいい。→平方根を出す
    sqrt = int(N**0.5)

    # 1とN以下の整数で割れるか確認→割れる場合あまりが0
    for i in range(2, sqrt+1):
        if N % i == 0:
            return False
    return True


# 標準入力
N = int(input())
print("Yes" if isPrime(N) else 'No')
