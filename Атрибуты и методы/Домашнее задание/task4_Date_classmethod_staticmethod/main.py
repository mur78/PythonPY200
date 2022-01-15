class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        # TODO
        if year % 4 == 0:
            print("Год високосный")
        else:
            raise ValueError()



    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        # TODO

    @staticmethod
    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        # TODO
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError()
        if day > 31 or month > 12:
            raise ValueError()


if __name__ == "__main__":
    # Write your solution here
    pass
