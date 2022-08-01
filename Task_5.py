# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний
#  элемент, второй и предпоследний и т.д.

from random import randint
import math

lst_number = [randint(0,10)for x in range(5)]
print(lst_number)

def product_list(nums):
    return [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]
product_list = lambda nums: [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]

print('Произведение пар чисел в списке:', product_list(lst_number))