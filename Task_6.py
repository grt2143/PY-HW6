#6-Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = 5

def get_seq(n):
    return [-3 **i for i in range(1, n+1)]

get_seq = lambda n: [-3 **i for i in range(1, n+1)]

print(get_seq(n))