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
