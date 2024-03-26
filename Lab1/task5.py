def head_pow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        if n < 0:
            x = 1 / x
            n = -n
        temp = head_pow(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x


def tail_pow(x, n, res=1):
    if n == 0:
        return res
    elif n == 1:
        return x * res
    if n < 0:
        x = 1 / x
        n = -n
    res *= x
    return tail_pow(x, n - 1, res)


while(True):
    x, n = float(input('Введіть число: ')), int(input('Введіть степінь: '))
    if (-100 < x < 100) and (pow(-2, 31) <= n <= pow(2, 31) - 1) and (-pow(10, 4) <= pow(x, n) <= pow(10, 4)):
        print('Головна рекурсія: ' + str(head_pow(x, n)))
        print('Хвостова рекурсія: ' + str(tail_pow(x, n)))
        break
    else:
        print('-100 < x < 100')
        print('-2 pow(31) <= n <= 2 pow(31)-1')
        print('-10 pow(4) <= x pow(n) <= 10 pow(4)')
