ru_char = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en_char = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
message = input("Введите сообщение на русском: ")  # Ввод сообщения на русском
k = 1
total = ""

for i in message:
    place = ru_char.find(i)  # Ищет символы из русского алфавита
    new_place = place + k  # Плюс один сдвиг (единица)
    if i in ru_char:
        total += ru_char[new_place]  # Сдвигает вправо на один символ
print(total)  # Вывод

for j in message:
    place1 = en_char.find(j)  # Ищет символы из английского алфавита
    if j in en_char:  # Если сообщение состоит из английских символов
        print("Вводи сообщение на русском!")
        break
