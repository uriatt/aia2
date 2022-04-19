__all_=['start_engine','stop_engine']
class Cars :
    def __init__(self,title, model, weight, hp, number, max_speed,color):
        self.title=title
        self.model=model
        self.weight=weight
        self.hp=hp
        self.number=number
        self.max_speed=max_speed
        self.color=color

    def start_engine(self):
        print(f"Engine on {self.title} {self.model}  started!")

    def stop_engine(self):
        print(f"Engine on{self.title}{self.model}  stoped!")
bmw=Cars(' BMW ',' M135iDrive ', 3306.9 ,'306hp ',777777 ,'250km/h ',' black')
bmw.start_engine()
bmw.stop_engine()

mercedes=Cars('Mercedes-Bens','S-CLASS','W221','4,310',8888888,'250km/h','white')
mercedes.start_engine()
mercedes.stop_engine()
