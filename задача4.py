# Задача 4: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n, m, k = int(input('n:')), int(input('m:')), int(input('k:'))
print(['NO', 'YES'][not (k % n and k % m)])