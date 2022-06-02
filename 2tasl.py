#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

#Пример:

#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

from random import randint
from unittest import result

def multiplication(new_list):
    result = []
    while len(new_list) > 1 :
        result.append(new_list[0]*new_list[-1])
        del new_list[0]
        del new_list[-1]
    if len(new_list) ==1: result.append(new_list[0]*new_list[0])
    return result

size = randint(1,10)
list = [randint(-100, 100) for i in range(size)]

print(f'Список случайных чисел: {list}')
print(f'Произведение пар списка: {multiplication(list)}')