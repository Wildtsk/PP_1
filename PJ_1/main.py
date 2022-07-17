from PJ_1.utils import generates_numbers, result_comparison, compares_received_numbers

generate_number = generates_numbers()
print(generate_number)
print('игра началась,\nя уже загадал трехзначное число, попробуй его отгадать')
while True:
    word = input()
    if word == "стоп":
        exit()
    received_numbers = compares_received_numbers(generate_number, word)
    print(result_comparison(received_numbers))
