
while True:
    n = input('請輸入正整數: ')
    if n == 'q':
        break
    n = int(n)
    x = 2
    if n == 1:
        print(n, '不是質數\n')
    while n != 1:
        if n % x != 0:
           x += 1
        elif n % x == 0:
            if n == x:
                print(n, '是質數\n')
                break
            else:
                print(n, '不是質數\n')
                break

