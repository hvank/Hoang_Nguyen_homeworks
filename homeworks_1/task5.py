# Вычислить сумму цифр случайного трёхзначного числа.(прочитать про
# модуль math и random).

import random
num = random.randint(100, 999)
print('Случайное число: ', num)
sum = sum(int(sum1) for sum1 in str(num))
print('Сумма цифр случайного числа: ', sum)