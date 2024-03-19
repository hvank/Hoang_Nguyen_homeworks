# Вычислить сумму цифр случайного трёхзначного числа (тут необходимо
# применить работу со строками)

import random
num = random.randint(100, 999)
print(num)
num_str = str(num)
sum_num = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
print(sum_num)