#    Вводится целое число (любого размера).
#    Написать функцию, которая разобьет это число на разряды символом "пробел",
#    Функция возвращает тип данных str
#    1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`


def format_number(number: str) -> str:
    result = []
    number = list(number)
    number.reverse()

    for i in range(len(number)):
        if i != 0 and i % 3 == 0:
            result.append(' ')
        result.append(number[i])

    result.reverse()
    return ''.join(result)


n = input('Enter number: ')
print('Formatted number: ' + format_number(n))
