import doctest

class Chair:
    def __init__(self, material, color):
        """
        Создание и подготовка к работе объекта "Стул"

        :param material: материал стула
        :param color: цвет стула

        Примеры:
        >>> chair = Chair('wood', 'brown')  # инициализация экземпляра класса
        """

        if not isinstance(material, str):
            raise TypeError("Материал только строкового типа")
        elif not isinstance(color, str):
            raise ValueError("Цвет должен быть не нулевого значения и строкой")

        self.material = material
        self.color = color

    def change_color(self, color: str) -> None:
        """
        Функция которая меняет цвет стула

        :param color: цвет стула

        :return: цвет стула

        Примеры:
        >>> chair = Chair('wood', 'brown')
        >>> chair.change_color('yellow')
        """
        ...

    def change_material(self, material: str) -> None:
        """
        Функция которая меняет материал стула

        :param material: материал стула

        :return: материал стула

        Примеры:
        >>> chair = Chair('wood', 'brown')
        >>> chair.change_material('steel')
        """
        ...


class Car:
    def __init__(self, brand, model, year_of_manufacture):
        """
        Создание и подготовка к работе объекта "Машина"

        :param brand: бренд машины
        :param model: модель машины
        :param year_of_manufacture: год выпуска

        Примеры:
        >>> car = Car('BMW', 'M3', 2004)  # инициализация экземпляра класса
        """

        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        elif not isinstance(model, str):
            raise ValueError("Значение строки не должно быть пустым")

        if year_of_manufacture < 0:
            raise ValueError("Год производства не должен быть отрицательным числом")

        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture

    def start(self):
        """
        Функция которая заводит авто

        :return: авто заведено

        Примеры:
        >>> car = Car('BMW', 'M3', 2004)
        >>> car.start()
        """
        ...

    def speed(self, speed: float) -> None:
        """
        Функция которая ускоряет авто на заданное число

        :return: скорость авто

        Примеры:
        >>> car = Car('BMW', 'M3', 2004)
        >>> car.speed(10)
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if speed < 0:
            raise ValueError("Скорость не может быть меньше нуля")
        ...

    def brake(self):
        """
        Функция которая останавливает авто

        :return: авто остановлено

        Примеры:
        >>> car = Car('BMW', 'M3', 2004)
        >>> car.brake()
        """
        ...


class Game:
    def __init__(self, name, genre, platform):
        """
        Создание и подготовка к работе объекта "Игра"

        :param name: название игры
        :param genre: жанр игры
        :param platform: платформа для игры

        Примеры:
        >>> game = Game('Bloodborne', 'Soulslike', 'PS4')  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")

        if not isinstance(genre, str):
            raise ValueError("Жанр игры не должен быть ничем")

        if platform not in ["PC", "PS4", "Mobile"]:
            raise ValueError("Платформа должна быть 'PC', 'PS4', or 'Mobile'")

        self.name = name
        self.genre = genre
        self.platform = platform

    def play(self):
        """
        Функция которая начинает игру

        :return: игра включена

        Примеры:
        >>> game = Game('Bloodborne', 'Soulslike', 'PS4')
        >>> game.play()
        """
        ...

    def save_progress(self):
        """
        Функция которая сохраняет игру

        :return: игра сохранена

        Примеры:
        >>> game = Game('Bloodborne', 'Soulslike', 'PS4')
        >>> game.save_progress()
        """
        ...

    def load_save(self):
        """
        Функция которая загружает игру

        :return: игра загружена

        Примеры:
        >>> game = Game('Bloodborne', 'Soulslike', 'PS4')
        >>> game.load_save()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
