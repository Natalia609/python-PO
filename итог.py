class Animal:
    """Базовый класс для представления животных в зоологической системе.

    Attributes:
        name (str): Название животного
        _age (int): Возраст животного в годах (защищённый атрибут)

    Methods:
        move(): Описывает базовый способ перемещения
        sound(): Возвращает базовый звук животного
    """

    def __init__(self, name: str, age: int) -> None:
        """Инициализирует экземпляр Animal.

        Args:
            name: Название животного
            age: Начальный возраст в годах
        """
        self.name = name
        self._age = age  # Инкапсуляция для контроля валидности значения

    def __str__(self) -> str:
        return f"{self.name} ({self._age} лет)"

    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, age={self._age!r})"

    def move(self) -> None:
        """Выводит базовое описание перемещения."""
        print(f"{self.name} перемещается")

    def sound(self) -> str:
        """Возвращает базовый звук животного."""
        return "Издаёт звук"

    def update_age(self, new_age: int) -> None:
        """Безопасное обновление возраста с валидацией."""
        if new_age > 0:
            self._age = new_age


class Bird(Animal):
    """Класс птиц, наследуется от Animal.

    Добавляет специфичные для птиц атрибуты:
        wingspan (float): Размах крыльев в метрах

    Methods:
        fly(): Уникальный метод для птиц
        move(): Перегрузка базового метода
    """

    def __init__(self, name: str, age: int, wingspan: float) -> None:
        super().__init__(name, age)
        self.wingspan = wingspan

    def __str__(self) -> str:
        return f"{super().__str__()} | Размах крыльев: {self.wingspan} м"

    def __repr__(self) -> str:
        return f"Bird(name={self.name!r}, age={self._age!r}, wingspan={self.wingspan!r})"

    def move(self) -> None:
        """Перегрузка метода для описания полёта.

        Причина перегрузки: способ перемещения птиц отличается от базового
        """
        print(f"{self.name} летит")

    def sound(self) -> str:  # Перегрузка (переопределение) метода
        return "Чирикает"  # Новая реализация для птиц

    def fly(self) -> str:
        """Уникальный метод для птиц."""
        return f"Летит с размахом крыльев {self.wingspan} метра"


class Fish(Animal):
    """Класс рыб, наследуется от Animal.

    Добавляет специфичные для рыб атрибуты:
        max_depth (float): Максимальная глубина погружения

    Methods:
        swim(): Уникальный метод для рыб
        sound(): Перегрузка базового метода
    """

    def __init__(self, name: str, age: int, max_depth: float) -> None:
        super().__init__(name, age)
        self.max_depth = max_depth

    def __repr__(self) -> str:
        return f"Fish(name={self.name!r}, age={self._age!r}, max_depth={self.max_depth!r})"

    def sound(self) -> str:
        """Перегрузка метода, т.к. рыбы издают другие звуки."""
        return "Булькает"

    def swim(self) -> str:
        """Уникальный метод для рыб."""
        return f"Погружается на глубину {self.max_depth} метров"