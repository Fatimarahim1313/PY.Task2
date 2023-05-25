# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import math
n=int(input('Введите число N: '))
count = 0
while n > 0:
    r = math.pow(2, count)
    if r <= n:
        print(f"{r}", end=' ')
    else:
        break
    count += 1