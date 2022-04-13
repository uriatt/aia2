class Person:
    def init(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
class Jack(Person):
    def init(self,first_name,last_name,phone_number,balance):
        super().init(first_name,last_name)
        self.phone_number=phone_number
        self.balance=balance

class Vito(Jack):

    def init(self, first_name, last_name, phone_number, balance):
        super().init(first_name, last_name, phone_number, balance)

    _n = 50
    def info_balance(self):
            c = 250 -n
            f = c + self.balance
            self.balance = f
            print(self.balance)

Jack = Person('Jack', 'Nieck', 2345, 100)
Vito = Jack('Vito', 'Roland', '3456', 10)
Vito.info_balance()



