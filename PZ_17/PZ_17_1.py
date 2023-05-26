# Создайте класс «Книга», который имеет атрибуты название, автор и количество страниц.
# Добавьте методы для чтения и записи книги.

class Book:

    # Инициализация экземпляря класса

    def __init__(self, name, author, quan):
        self.name = name
        self.author = author
        self.quan = quan

    # Чтение книги

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_quan(self):
        return self.quan

    # Запись книги

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_quan(self, quan):
        self.quan = quan


a = Book("Мистер Мерседес", "Стивен Кинг", 400)
print(a.get_author())
print(a.get_name())
print(a.get_quan())