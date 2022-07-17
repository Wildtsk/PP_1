import random


def generates_numbers():
    """Геренрирует 3 рандомных числа"""
    numbers = '0123456789'
    result_number = []
    for i in range(0, 3):
        result_number += random.sample(numbers, 1)
    return result_number


def compares_received_numbers(generate_number, number: str) -> list:
    """Получает 3х значное число от пользователя. Сравнивает полученные числа с загаданным"""
    result = []
    ind = 0
    for num in number:
        if num in generate_number:
            if num == generate_number[ind]:
                result.append('Fermi')
            else:
                result.append('Pico')
        ind += 1
    return result


def result_comparison(received_numbers):
    """Выводит результат сравнения"""
    if len(received_numbers) == 0:
        result = 'Bagels'
    else:
        result = ', '.join(received_numbers)
    return result
