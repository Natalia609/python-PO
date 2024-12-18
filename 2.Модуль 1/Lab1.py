# TODO Написать 3 класса с документацией и аннотацией типов

import doctest
class Pencil:
    def __init__(self, sost_pencil: bool, stepen_toch: int):
        """
               Создание и подготовка к работе объекта "Карандаш"

               :param sost_pencil: Наточен ли карандаш
               :param stepen_toch: Степень наточенности карандаша в процентах

               Примеры:
               >>> sost = Pencil(1, 0)  # инициализация экземпляра класса
               """
    def is_pencil_ostry(self)->bool:
        """
                Функция которая проверяет является ли карандаш острым

                :return: Является ли карандаш острым

                Примеры:
                >>> sost = Pencil(1, 0)
                >>> sost.is_pencil_ostry
                """
        ...

    def tochit_pencil(self, tochit: int) -> None:
        """
        Заточка карандаша, если sost=0 или sost=1 и stepen_toch<20 .
        :param tochit: обавляемый процент заточки

        Примеры:
        >>> sost = Pencil(1, 0)
        >>> sost.tochit_pencil(30)
        """

        ...

    def write_pencil(self, estimate_toch: int) -> None:
        """
        Пишем карандашом если заточка нас устраивает.

        :param estimate_toch: Истощаем процент заточки


        :return: состояние оставшейся заточки карандаша

        Примеры:
        >>> sost = Pencil(1, 80)
        >>> sost.write_pencil(20)
        """
        ...

class Chest:
    def __init__(self, napoln: bool, stepen_napoln: int):
        """
               Создание и подготовка к работе объекта "Сундук"

               :param napoln: Пуст ли сундук
               :param stepen_napoln: Процент наполненности

               Примеры:
               >>> sost = Chest(1, 0)  # инициализация экземпляра класса
               """
    def is_chest_empty(self)->bool:
        """
                Функция которая проверяет является ли сундук пустым

                :return: Является ли сундук пустым

                Примеры:
                >>> sost = Chest(1, 0)
                >>> sost.is_chest_empty
                """
        ...

    def add_smt(self, smt: int) -> None:
        """
        Добавляет процент заполненности .
        :param smt: обавляемый процент заполненности

        Примеры:
        >>> sost = Chest(1, 0)
        >>> sost.add_smt(30)
        """

        ...

    def remove(self, proc: int) -> None:
        """
        Опустошаем сундук на процент.

        :param proc: Процент на который опустошаем


        :return: заполненность сундука

        Примеры:
        >>> sost = Chest(1, 80)
        >>> sost.remove(20)
        """
        ...
class Russian_doll:
    def __init__(self, full: bool, colvo: int):
        """
               Создание и подготовка к работе объекта "Матрёшка"

               :param full: Собранна ли матрёшка
               :param colvo: сли она разобрана, сколько звеньев собранно, max:8
               если full=0, colvo не может быть равно 8

               Примеры:
               >>> sost = Russian_doll(0, 3)  # инициализация экземпляра класса
               """
    def Russian_doll_full(self)->bool:
        """
                Функция которая проверяет является ли матрёшка собранной

                :return: Является ли матрёшка собранной

                Примеры:
                >>> sost = Russian_doll(0, 3)
                >>> sost.Russian_doll_full
                """
        ...

    def add_mini(self, smt: int) -> None:
        """
        Добавляет некоторое количество звеньев в матрёшку .
        :param smt: количество звеньев

        Примеры:
        >>> sost = Russian_doll(0, 3)
        >>> sost.add_mini(2)
        """

        ...

    def remove(self, insides: int) -> None:
        """
        убираем звенья из матрёшки.

        :param insides: количество звеньев


        :return: состояние матрёшки

        Примеры:
        >>> sost = Russian_doll(1, 0)
        >>> sost.remove(5)
        """
        ...

    if __name__ == "__main__":
        doctest.testmod()
