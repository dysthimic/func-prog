def head_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return head_fibonacci(n - 1) + head_fibonacci(n - 2)


def tail_fibonacci(n, prev=0, curr=1):
    if n == 0:
        return prev
    elif n == 1:
        return curr
    else:
        return tail_fibonacci(n - 1, curr, prev + curr)


n = 4
print('F(' + str(n) + ')')
print('Головна рекурсія: ' + str(head_fibonacci(n)))
print('Хвостова рекурсія: ' + str(tail_fibonacci(n)))
