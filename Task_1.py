# 1- Определить, присутствует ли в заданном списке строк, 
# некоторое число

lst_number = ['2a','10rt','3we','5','7']

number1 = int(input("Введите искомое число: "))  
result = list(filter(lambda element: str(number1) in element, lst_number))
print(result)