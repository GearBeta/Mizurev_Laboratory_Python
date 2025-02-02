class Book:
    """ Базовый класс книги. """

    def init(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"Книга {self.name}. Автор {self.author}"

    def repr(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().init(name, author)
        self._pages = None
        self.pages = pages  # Используем setter для валидации

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self._pages = value

    def str(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    def repr(self):
        return f"{self.__class__.name}(name={self.name!r}, author = {self.author!r}, pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().init(name, author)
        self._duration = None
        self.duration = duration  # Используем setter для валидации

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Продолжительность должна быть числом с плавающей запятой.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = value

    def str(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

    def repr(self):
        return f"{self.__class__.name}(name={self.name!r}, author = {self.author!r}, duration = {self.duration!r})"