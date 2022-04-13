
class Person:
    def init(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    def init(self, first_name, last_name, phone_number, balance):
        super().init(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


class Vito(Jack):
    _n = 50


    def init(self, first_name, last_name, phone_number, balance):
        super().init(first_name, last_name, phone_number, balance)


    def info_balance(self):
        c = 250 - self._n
        f = c + self.balance
        self.balance = f
        print(self.balance)
Jack2 = Person('Jack', 'Nieck')
Jack1 = Jack('Vito', 'Roland', '3456', 10)
vito = Vito('Vito', 'Roland', '3456', 10)
vito.info_balance()
vito.info_balance()
vito.info_balance()
vito.info_balance()
