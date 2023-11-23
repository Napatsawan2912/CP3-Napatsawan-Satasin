class Vehicle:
    LicenseCode = ""
    SerialCode = ""

    def TurnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    color = ""

class PickUp(Vehicle):
    color = ""

class Van(Vehicle):
    color = ""

class EstateCar(Vehicle):
    color = ""

Car1 = Car()
Car1.TurnOnAirConditioner()
Car1.color = "red"

PickUp1 = PickUp()
PickUp1.TurnOnAirConditioner()
PickUp1.color = "blue"

Van1 = Van()
Van1.TurnOnAirConditioner()
Van1.color = "green"

EstateCar1 = EstateCar()
EstateCar1.TurnOnAirConditioner()
EstateCar1.color = "yellow"