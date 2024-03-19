# Напиши программу, которая принимает строку от пользователя и выводит
# все слова этой строки в обратном порядке

text = input('Введите текст: ')
text_split = text.split()
text_split = text_split[::-1]
text_new = ' '.join(text_split)
print(text_new)