import random  # Импортируем модуль случайных значений

ru_char = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en_char = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
digit = "0123456789"
let = ru_char + en_char + digit  # Превращаем наши три словаря в один

C = random.choice(let)  # Случайный элемент из словаря
print("Символ: ", C)
if ru_char.find(C) != -1:  # Если элемент русский
    print("rus")
elif en_char.find(C) != -1:  # Если элемент английский
    print("lat")
elif digit.find(C) != -1:  # Если элемент цифра
    print("digit")
