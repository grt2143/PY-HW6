#3- Найти расстояние между двумя точками пространства
# (числа вводятся через пробел)


a = list(map(int, input('Введите координаты первой точки: ').split()))
b = list(map(int, input('Введите координаты второй точки: ').split()))
def dist(x,y):
    return (sum(map(lambda xx,yy : (xx-yy)**2,x,y)))**0.5
print(dist(a,b))