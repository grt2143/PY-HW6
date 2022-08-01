# 2- Найти сумму чисел списка стоящих на нечетной позиции

lst_number = [5, 2, 1, 3, 6, 9, 7]
print(lst_number)

def sum_list(lst_number: list):
    sum_of_number = 0
    for i in list(filter(lambda x : lst_number.index(x)%2 != 0, lst_number)):
        sum_of_number += i
    return sum_of_number

print(f'Сумма чисел списка стоящих на нечетной позиции: {sum_list(lst_number)}')