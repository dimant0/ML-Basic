# Написать функцию, которая принимает на вход квадратное уравнение (одной строкой) и возвращает его корни, либо сообщает, что их нет
# "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7

import math


def calculate_square_equation(equation: str) -> str:
    if '=' not in equation:
        return 'Это не квадратное уравнение'

    eq = equation.replace(' ', '')
    e_list = list(eq)

    if e_list[0] == 'x':
        coef = eq.split('*x')
        coef[0] = coef[0].replace('x**2', '')
        coef.insert(0, '1')
    else:
        coef = eq.split('*x')

    coefs = {}
    for i in range(len(coef)):
        if i == 0:
            if '**2' in coef[i]:
                a_coef = float(coef[i].replace('**2', ''))
            else:
                a_coef = float(coef[i])

            if '-' in coef[i]:
                coefs['a'] = (-1) * a_coef
            else:
                coefs['a'] = a_coef
        elif i == 1:
            item = coef[i].replace('**2', '')
            if '-' in coef[i]:
                coefs['b'] = (-1) * float(item.replace('-', ''))
            else:
                coefs['b'] = float(item.replace('+', ''))
        elif i == 2 and '=0' in coef[i]:
            item = coef[i].replace('=0', '')
            if '-' in coef[i]:
                coefs['c'] = (-1) * float(item.replace('-', ''))
            else:
                coefs['c'] = float(item.replace('+', ''))

    discriminant = coefs['b'] ** 2 - 4 * coefs['a'] * coefs['c']
    if discriminant < 0:
        return f'Уравнение: "{equation}" -> не имеет действительных корней'

    x_1 = ((-1) * coefs['b'] + math.sqrt(discriminant)) / 2 * coefs['a']
    x_2 = ((-1) * coefs['b'] - math.sqrt(discriminant)) / 2 * coefs['a']

    return f'Уравнение: "{equation}" -> x_1 = {x_1}, x_2 = {x_2}'


print(calculate_square_equation('x**2 - 11*x + 28 = 0'))
print(calculate_square_equation('4*x**2 - 3*x + 1 = 0'))
print(calculate_square_equation('5*x**2 + 3*x - 26 = 0'))
