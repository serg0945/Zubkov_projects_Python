Entry = input("Введите что-нибудь: ")


def findlen(entry):  # Считает длину строки
    a = 0
    for i in entry:
        a += 1
    return a


print("Число символов в строке:", findlen(Entry))
