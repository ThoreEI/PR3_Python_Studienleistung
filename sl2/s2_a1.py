class Fahrzeug:
    pass


class Auto(Fahrzeug):
    pass


class BondCar(Fahrzeug, Auto):
    pass


if __name__ == "__main__":
    g = BondCar()
