#
#    Написать функцию, которая заменяет принимает строку текста и изменяет снейк_кейс на КамелКейс и наоборот
#    my_first_func -> MyFirstFunc, AnotherFunction -> another_function
#


def trans_caser(string: str) -> str:
    if type(string) is not str:
        return string

    str_list = list(string)
    if not str_list:
        return string

    if str_list[0].isupper():
        delimeters = []

        for i in range(len(str_list)):
            if str_list[i].isupper():
                delimeters.append(i)

        del delimeters[0]  # перед первым символом разделитель не ставим

        j = 0
        for i in range(len(str_list)):
            if i in delimeters:
                str_list.insert(i + j, '_')
                j += 1

        str_list = [i.lower() for i in str_list]
        string = ''.join(str_list)
        return string
    else:
        to_upper_flag = False
        for i in range(len(str_list)):
            if to_upper_flag:
                str_list[i] = str_list[i].upper()
                to_upper_flag = False
            if str_list[i] == '_':
                to_upper_flag = True
        str_list = [letter for letter in str_list if letter != '_']
        str_list[0] = str_list[0].upper()
        string = ''.join(str_list)
        return string



print(trans_caser(1))
print(trans_caser([1,2,3]))

print(trans_caser('VeryVeryLongNameOfFunction'))
print(trans_caser('MyFirstFunc'))

print(trans_caser('my_first_func'))
print(trans_caser('very_long_parameter_for_the_my_func'))
