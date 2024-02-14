# Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int).
# Результат выполнения функции - шифрованное слово по методу Шифр Цезаря. Написать вторую функцию,
# которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)

# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'


def encrypt(string: str, key: int) -> str:
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for letter in string:
        index = alfabet.find(letter)
        key_index = index + key
        if key_index > len(alfabet):
            diff = len(alfabet) - key_index
            result.append(alfabet[abs(diff)])
        else:
            result.append(alfabet[key_index])
    string = ''.join(result)
    return string


def decrypt(encrypted_string: str, key: int) -> str:
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for letter in encrypted_string:
        index = alfabet.find(letter)
        key_index = index - key
        result.append(alfabet[key_index])
    string = ''.join(result)
    return string



print('dog -> ' + encrypt('dog', 3))
print('grj -> ' + decrypt('grj', 3))
print('')
print('python -> ' + encrypt('python', 5))
print('udymts -> ' + decrypt('udymts', 5))
print('')
print('test -> ' + encrypt('test', 30))
print('xiwx -> ' + decrypt('xiwx', 30))