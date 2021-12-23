from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Ошибка типа")
        if capacity_volume <= 0:
            raise ValueError("Ошибка значения")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Ошибка типа")
        if occupied_volume <= 0:
            raise ValueError("Ошибка значения")




        #  TODO инициализировать объект "Стакан"
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(200, 100)  # TODO инициализировать два объекта типа Glass
    glass_2 = Glass(150.0, 80.0)
    glass_3 = Glass("100", 120)

    # TODO попробовать инициализировать не корректные объекты
    print(glass_1)
    print(glass_2)
    print(glass_3)