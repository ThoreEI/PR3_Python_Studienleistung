class Vehicle:
    def __init__(self, tires) -> None:
        self._tires: int = tires


class Car(Vehicle):
    def __init__(self, engine):
        super().__init__(tires=4)
        self._engine: str = engine


class SportCar(Vehicle, Car):
    def __init__(self, max_speed):
        super().__init__(engine="Fast")
        self._max_speed: float = max_speed


if __name__ == "__main__":
    porsche_911 = SportCar(max_speed=280.45)
