1. Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2

a = 15*3
print (type (a))

b = 15/3
print (type (b))

c = 15//3
print (type (c))

d = 15**3
print (type (d))

# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!





e = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
e1:int = len(e)


for _ in range(e1):

    elem = e.pop(0)

    if elem.isdigit() and elem.isalnum():  # no nessary use isalnum in here but I use
        e.append(f'"{int(elem):02d}"')


    elif elem[0] == "+" and elem[1].isdigit():
        e.append(f'"+{int(elem):02d}"')

    else:
        e.append(elem)

print(' '.join(e))

# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
#
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' Подумать,
# как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

h = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

answer = {}

for string in h:
    i = string.split()[-1].capitalize()
    print(f"Привет, {i}!")

# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

g = [57.8, 46.51, 97, 76.05, 13.11, 87.93, 27, 97.09, 0.16, 42,
        96.64, 34.17, 97.45, 40.62, 84.94, 7, 52.23, 93.74, 89, 3.93]

store_id = id(g)
print(g)

print(f"{'a':-^100}")

end_word:str = ", "

for i, num in enumerate(g):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(g) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)


print(f"{'b':-^100}")

print(f"id before sort {store_id}")
g.sort()
print(g)
print(f"id after sort {id(g)}")

if store_id == id(g):
    print("In place")
else:
    print("Diff obj")


print(f"{'c':-^100}")

g1 = g.copy()
g1.sort(reverse=True)

print(g1)
print(store_id)
print(id(g1))

if store_id == id(g1):
    print("In place")
else:
    print("Diff obj")


print(f"{'d':-^100}")


print("five biger prices", g [-6:-1]) 

