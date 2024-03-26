def head_climb(n):
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    elif n == 2:
        return 2
    else:
        return head_climb(n - 1) + head_climb(n - 2)


def tail_climb(n, prev=1, curr=1):
    if n == 0:
        return 0
    elif n <= 1:
        return curr
    else:
        return tail_climb(n - 1, curr, prev + curr)


while(True):
    n = int(input('Введіть кількість кроків: '))
    if n >= -1 and n <= 45:
        print('К-ість комбінацій:')
        print('Головна рекурсія = ' + str(head_climb(n)))
        print('Хвостова рекурсія = ' + str(tail_climb(n)))
        break
    else:
        print('Обмеження: -1 <= n <= 45')
