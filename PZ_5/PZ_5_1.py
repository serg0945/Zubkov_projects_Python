entry = input("Введите что-нибудь: ")


def findlen(def_entry):  # Считает длину строки
    count = 0
    while count < len(def_entry):  
        count += 1
    return count


print("Число символов в строке:", findlen(entry))
