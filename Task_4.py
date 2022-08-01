# 4- Определить, позицию второго вхождения строки в списке либо
#  сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


Lst_num = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num = 'qwe'
def second_coming(lst:list, num:int):
    lst = []
    num = ''
    return [i for i, element in enumerate(lst) if num in element][1]if len(lst) > 2 else 0
list_new = ([i for i, element in enumerate(Lst_num) if num in element][1]if len(Lst_num) > 2 else 0)
print(list_new)