"""
Составить генератор (yield), который преобразует все буквенные символы в строчные.
"""
text = input("Введите какой-нибудь текст, который весь будет переведён в нижний регистр: ")


def text_lower(lower):
    for i in lower:
        yield i.lower()


print(''.join(text_lower(text)))

