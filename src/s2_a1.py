class Vehicle:
    def __init__(self, tires):
        self.__tires: int = tires


class Car(Vehicle):
    def __init__(self, engine):
        super().__init__(tires=4)
        self.__engine: str = engine


class RocketCar(Vehicle, Car):
    def __init__(self, max_speed):
        super().__init__(engine="Rocket engine")
        self.__max_speed: float = max_speed


if __name__ == "__main__":
    RocketCar(max_speed=700)
