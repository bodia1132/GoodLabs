# Константи
var_1 = True
print(var_1)
var_2 = None
print(var_2, '\n')

# Результати роботи простих функцій
print('Function dir() = ',dir())
dict_print = dict([('a', 1), ('b', -1)])
print('Function dict() = ', dict_print)

# цикл
count = range(10)
for i in count:
    print("i = ", i)

# розгалуження
input = int(input("\nВведіть номер лабораторної: "))
if input >= 3:
    print("Лабораторна робота не була зарахована\n")
else:
    print("Зараховано\n")

# конструкція try->except->finally
number = 0
try:
    arr = [1, 2, 3, 4, 5]
    value = arr[6]
except IndexError:
    print("Не знайдено елементу в масиві.")
finally:
    print("Результат.\n")

# контекст-менеджер with
with open("file.txt", 'r+') as file:
    file.write('text')
    file.close()

# lambda
arr1 = list(range(1, 20, 2))
lamb = list(map(lambda x: x * 2, arr1))
print(lamb, "\n")
