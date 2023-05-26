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
