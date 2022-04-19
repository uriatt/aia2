class Cars:
    def __init__(self, title, model, weight, hp, number, max_speed, color):
            self.title = title
            self.model = model
            self.weight = weight
            self.hp = hp
            self.number = number
            self.max_speed = max_speed
            self.color = color

    def _get_info(self,weight,hp):
        print(f"""
        Title:{self.title}
        Model:{self.model}
        Weight:{weight}
        Hp:{hp}
        Number:{self.number}
        max_speed:{self.max_speed}
        color:{self.color}
""")
bmw=Cars(' BMW ',' M135iDrive ', 3306.9 ,'306hp ',777777 ,'250km/h ',' black')
bmw._get_info(2356.2,'345hp')

mercedes=Cars('Mercedes-Bens','S-CLASS','W221','4,310',8888888,'250km/h','white')
mercedes._get_info(3809.2,'272hp')