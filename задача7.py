# Задача 7: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
m = 1
while m < n:
    print (m,end=' ')
    m = m * 2