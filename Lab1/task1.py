def head_reverse(str):
    if len(str) == 0:
        return str
    else:
        return head_reverse(str[1:]) + str[0]


def tail_reverse(str, reverse=''):
    if len(str) == 0:
        return reverse
    else:
        return tail_reverse(str[1:], str[0] + reverse)


str = 'tiger'
print('Текст: ' + str)
print('Головна рекурсія: ' + head_reverse(str))
print('Хвостова рекурсія: ' + tail_reverse(str))
