# SECRET_KEY = "RYEURUEIOHDFDCVKDC*8"
#
#
# def test(text):
#     print(text)
class Person:
    def __init__(self,first_name,last_name,age,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.salary=salary
    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"