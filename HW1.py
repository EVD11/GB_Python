#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры:
#
#duration = 53
#53 сек
#2 мин 33 сек
#duration = 4153
#1 час 9 мин 13 сек
#duration = 400153
#4 дн 15 час 9 мин 13 сек
#
#Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?

#t = int(input('Введи число: '))
#d, h, m, s = t // 86400, t // 3600, t // 60 % 60, t % 60
#print(f'{d} дней {h} час {m} мин {s} cек')

# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!

cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print('Cписок кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]



# b.  К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# c.  * Решить задачу под пунктом b, не создавая новый список.

