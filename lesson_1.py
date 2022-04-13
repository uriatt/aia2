####что такое оопе:
#klass
class Transport:
    def __init__(self,tittle,model,type,year):
        self.tittle=tittle
        self.model=model
        self.type=type
        self.year=year
bmw=Transport('BMW','e34','car',1990)##instance Transport
mercedes=Transport('Mercedes','w124','car',1990)#instance Transport



# class Dog:
#     def __init__(self,name,age,type):
#         self.name=name
#         self.age=age
#         self.type=type
#     def voice(self):
#         print(f"{self.name} gaf! gaf!")
#     def eat(self):
#         print(f"{self.name} I'am eating now")
#     def move(self):
#         print(f"{self .name} i am sleeping now")
#     def info(self, weight,height):
#         print(f"""
#         Name:{self.name}
#         Age:{self.age}
#         Type:{self.type}"
#         weight:{weight}
#         Height:{height}
#         """)
# rex=Dog('Rex' ,40, 'pitbul')
# rex.voice()
# rex.info(50,1.30)
# sharic=Dog('Sharik' , 20, 'pitpul')
# sharic.voice()
# sharic.eat()
# sharic.move()
# sharic.info(40,1.20)
# nana.info(80,1.70)