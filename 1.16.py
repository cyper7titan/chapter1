from tabulate import tabulate

list_of_digit = list()
data_input = input('Введите 4 числа через одинарный пробел - ')
for number in data_input.split(' '):
    list_of_digit.append(int(number))

print(tabulate([['a)', 5, 10, ' ', 'б)', 100, list_of_digit[0], ' ', 'в)', list_of_digit[2],25],\
                [' ', 7, 'sm', ' ', ' ', 1949, list_of_digit[1], ' ', ' ', list_of_digit[2], list_of_digit[3]]]))