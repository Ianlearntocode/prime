import time

def is_prime(n):
    if n == 1:
        return False
    else:
        x = 2
        while x ** 2 <= n:
            if n % x != 0:
                x += 1
            else:
                return False
        else:
            return True

def main():
    n_range = input('請輸入數字: ')
    n_range = int(n_range)
    start_time = time.time()
    prime_number = 0
    for i in range(1, n_range):
        if is_prime(i):
            prime_number += 1
    print(f'1~{n_range}共有{prime_number}個質數，計算總共花費{time.time() - start_time}秒')

main()