if __name__ == "__main__":

    class Car:
        """
        Базовый класс для автомобилей.
        Содержит общие атрибуты и методы для всех типов автомобилей.
        """

        def __init__(self, brand: str, model: str, year: int, price: float):
            """
            Инициализирует автомобиль с брендом, моделью, годом выпуска и ценой.

            brand: марка автомобиля (строка).
            model: модель автомобиля (строка).
            year: год выпуска (целое число).
            price: цена автомобиля (число с плавающей запятой).
            """
            self._brand = brand  # Непубличный атрибут
            self._model = model  # Непубличный атрибут
            self.year = year
            self.price = price

        def __str__(self) -> str:
            """
            Возвращает строковое представление автомобиля.

            Строка с маркой, моделью, годом и ценой автомобиля.
            """
            return f"{self._brand} {self._model}, {self.year}, ${self.price}"

        def __repr__(self) -> str:
            """
            Возвращает строку, подходящую для использования в отладочных целях.

            :return: строковое представление объекта.
            """
            return f"Автомобиль(Марка авто={self._brand!r}, модель={self._model!r}, год={self.year}, цена={self.price})"

        def get_info(self) -> str:
            """
            Метод для получения полной информации об автомобиле.

            Строка с полной информацией.
            """
            return f"Марка авто: {self._brand}, модель: {self._model}, год: {self.year}, цена: ${self.price}"


    class Sedan(Car):
        """
        Дочерний класс для легковых автомобилей (седан).
        """

        def __init__(self, brand: str, model: str, year: int, price: float, trunk_size: float):
            """
            Инициализирует седан с дополнительным атрибутом размера багажника.

            brand: марка автомобиля.
            model: модель автомобиля.
            year: год выпуска.
            price: цена автомобиля.
            trunk_size: размер багажника в литрах.
            """
            super().__init__(brand, model, year, price)  # Наследуем конструктор базового класса
            self.trunk_size = trunk_size  # Атрибут для размера багажника

        def __str__(self) -> str:
            """
            Перегружает строковое представление для легкового автомобиля.

            строка с маркой, моделью, годом, ценой и размером багажника.
            """
            return f"{self._brand} {self._model} (легковой автомобиль), {self.year}, ${self.price}, Объем багажника: {self.trunk_size} л."

        def get_info(self) -> str:
            """
            Перегружает метод получения информации для легкового автомобиля,
            добавляя информацию о размере багажника.

            строка с полной информацией.
            """
            base_info = super().get_info()  # Используем метод родительского класса
            return f"{base_info}, Объем багажника: {self.trunk_size} л."


    class Truck(Car):
        """
        Дочерний класс для грузовых автомобилей.
        """

        def __init__(self, brand: str, model: str, year: int, price: float, payload_capacity: float):
            """
            Инициализирует грузовой автомобиль с дополнительным атрибутом грузоподъемности.

            brand: марка автомобиля.
            model: модель автомобиля.
            year: год выпуска.
            price: цена автомобиля.
            payload_capacity: грузоподъемность в тоннах.
            """
            super().__init__(brand, model, year, price)  # Наследуем конструктор базового класса
            self.payload_capacity = payload_capacity  # Атрибут для грузоподъемности

        def __str__(self) -> str:
            """
            Перегружает строковое представление для грузового автомобиля.

            :return: строка с маркой, моделью, годом, ценой и грузоподъемностью.
            """
            return f"{self._brand} {self._model} (Грузовик), {self.year}, ${self.price}, Грузоподъемность: {self.payload_capacity} тонн."

        def get_info(self) -> str:
            """
            Перегружает метод получения информации для грузового автомобиля,
            добавляя информацию о грузоподъемности.

            строка с полной информацией.
            """
            base_info = super().get_info()  # Используем метод родительского класса
            return f"{base_info}, Грузоподъемность: {self.payload_capacity} тонн."


    # Пример использования:
    sedan = Sedan("Toyota", "Camry", 2023, 30000.00, 500)
    truck = Truck("Volvo", "FH16", 2022, 80000.00, 18)

    print(sedan)
    print(sedan.get_info())
    print(truck)
    print(truck.get_info())

    pass