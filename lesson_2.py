####абстрак клас деген бул чон атасы же super анын жазгандарын эрчигендер неберелери
"""

Abstract Class

"""


class Transport:

    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"Engine on {self.title} {self.model} started!")


class Car(Transport):

    def __init__(self, title, model,color, speed):
        super().__init__(title, model, color)
        self.speed = speed


class Airplane(Transport):

    def __init__(self, title, model, color, weight, height):
        super().__init__(title, model, color)
        self.weight = weight
        self.height = height

    def new_method(self):
        print("Its method in Airplane")


class DeliveryAirplane(Airplane):

    def __init__(self, title, model, color, weight, height, amount):
        super().__init__(title, model, color, weight, height)
        self.amount = amount


bmw = Car('BMW', 'e34', 'black', 340)
bmw.start_engine()

boing = Airplane('Boing', 'x232', 'white', 10000, 5.5)
boing.start_engine()
boing.new_method()
#####################

"""

Abstract Class

"""


class Transport:

    def __init__(self, title, model, color):
        self.title = title
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"Engine on {self.title} {self.model} started!")


class Car(Transport):
    _current_speed = 0
    _is_started = False

    def __init__(self, title, model, color, speed, max_speed):
        super().__init__(title, model, color)
        self.speed = speed
        self.max_speed = max_speed

    def _get_current_speed(self):
        print(self._current_speed)

    def _get_is_started(self):
        if not self._is_started:
            print("Start engine!!!!")
            return False
        else:
            return True

    def start_engine(self):
        self._is_started = True
        print(f"{self.title} {self.model} engine started! {self.speed}")

    def gas(self):
        started = self._get_is_started()

        if self._current_speed + self.speed <= self.max_speed and started:
            self._current_speed += self.speed
            self._get_current_speed()
        else:
            print("Check on!")

    def break_(self):
        started = self._get_is_started()
        if self._curr  ent_speed >= self.speed and started:
            self._current_speed -= self.speed
            self._get_current_speed()


bmw = Car('BMW', 'e38', 'black', 60, 560)
