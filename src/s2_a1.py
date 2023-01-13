class Vehicle:
    def __init__(self, tires) -> None:
        self.__tires: int = tires


class Car(Vehicle):
    def __init__(self, engine):
        super().__init__(tires=4)
        self.__engine: str = engine


class BondCar(Vehicle, Car):
    def __init__(self, max_speed: float):
        super().__init__(engine="Fast")
        self.__max_speed = max_speed


if __name__ == "__main__":
    bond_car = BondCar(123.45)
