if __name__ == "__main__":
    class ConstuctionStages:
        """Строительные этапы."""
        def __init__(self, strenght: float, time: str, materials: float):
            """
            Args:
                 strenght: Цена работ.
                 materials: Цена материалов.
                 time: Время на производство этапа.
            """
            if not isinstance(strenght, (int, float)):
                raise TypeError("Цена должна быть указана типом int или float")
            if strenght <= 0:
                raise ValueError("Цена работ должна быть положительным числом")
            self.strenght = strenght

            self.materials = materials
            if not isinstance(strenght, (int, float)):
                raise TypeError("Цена должна быть указана типом int или float")
            if strenght <= 0:
                raise ValueError("Цена материалов должна быть положительным числом")

            if strenght <= 0:
                raise ValueError("Время должно быть положительным")
            self.time = time

        def __str__(self) -> str:
            return f'Стоимость работ: {self.strenght}, стоимость материалов: {self.materials} срок этапа: {self.time}'

        def __repr__(self) -> str:
            return f'Стоимость работ: {self.strenght!r}, стоимость материалов: {self.materials!r} срок этапа: {self.time!r}'

        def is_payment_stage(self) -> bool:
            """
            Функция, которая проверяет, прошла ли оплата за этап
            :return: Прошла ли оплата
            """

    class Foundation(ConstuctionStages):
        def __init__(self, fitting: str, concrete: str, squere: int):
            super().__init__(self.strenght, self.time, self.materials)
            self.fitting = fitting
            self.concrete = concrete
            self.squere = squere

        def __str__(self) -> str:
            return f'Стоимость работ: {self.strenght}, стоимость материалов: {self.materials} срок этапа: {self.time}, площадь: {self.squere}'
    pass
