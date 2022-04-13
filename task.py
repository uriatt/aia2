# class Cow:
#     def __init__(self,name,age,color,species):
#         self.name=name
#         self.age=age
#         self.color=color
#         self.species=species
#     def voice(self):
#         print(f"{self.name} Muu,MUUU!")
#     def eat(self):
#         print(f"{self.name} I'am eating  grass!")
#     def sleep(self):
#         print(f"{self.name} I'll be sleep only at night!")
#     def child(self):
#         print(f"{self.name} one child")
#     def info(self,weight,height):
#         print(f"""
#         Name:{self.name}
#         Age:{self.age}
#         Color:{self.color}
#         Species:{self.species}
#         weight:{weight}
#         height:{height}
#
#         """)
#nana=Cow('nana',5,'black','milk species')
# voin=Cow('voin ',7,'braun','meat species')
# voin.info(120,1.78)
# voin.voice()
# nana.voice()
# nana.eat()
# nana.sleep()
# nana.child()
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def voice(self):
#         print(f"{self.name} Wuf,Wuf")
#     def eat(self):
#         print(f"{self.name} i like to eat a meat")
#
#     def children(self):
#         print(f"{self.name} i have 9 children")
#     def info(self,weight,height):
#         print(f"""
#         Name:{self.name}
#         age:{self.age}
#         Weight:{weight}
#         Height:{height}
#
# """)
# alabai=Dog('Alabai',5)
# alabai.voice()
# alabai.info(60,1.65)
# alabai.eat()
# alabai.children()
# pitbul=Dog('pitbul',8)
# pitbul.info(80,1.50)
# pitbul.voice()
# class Bear:
#     def __init__(self,name,age,voice_text):
#         self.name=name
#         self.age=age
#         self.voice_text=voice_text
#     def voice(self):
#         print(f"{self.name}{self.voice_text}")
#
#
# bear1=Bear('test',12,'TTTTTTTKKKKKLLL')
# bear1.voice()
class Car :
    def __init__(self,title, model, weight, hp, number, max_speed,color):
        self.title=title
        self.model=model
        self.weight=weight
        self.hp=hp
        self.number=number
        self.max_speed=max_speed
        self.color=color

    def start_engine(self):
        print(f"Engine on {self.title} {self.model} started!")

    def stop_engine(self):
        print(f"Engine on{self.title}{self.model} stoped!")
    # def stop_engine(self) :
    #     print(f"{self.title}{self.model} engine stoped!
    def all_info(self,weight,hp):
        print(f"""
        Title:{self.title}
        Model:{self.model}
        Weight:{weight}
        Hp:{hp}
        Number:{self.number}
        max_speed:{self.max_speed}
        color:{self.color}
""")
bmw=Car(' BMW ',' M135iDrive ', 3306.9 ,'306hp ',777777 ,'250km/h ',' black')
bmw.start_engine()
bmw.stop_engine()
bmw.all_info(3306.9,'306hp')
mercedes=Car('Mercedes-Bens','S-CLASS','W221','4,310',8888888,'250km/h','white')
bmw.start_engine()
bmw.stop_engine()
mercedes.all_info(3809.2,'272hp')
