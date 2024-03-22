score = int(input("Введите балл: "))

if score >= 85:
    grade = "Отлично"
elif score >= 70:
    grade = "Хорошо"
elif score >= 60:
    grade = "Удовлетворительно"
elif score >= 50:
    grade = "Достаточно"
else:
    grade = "Недостаточно"

print("Оценка:", grade)