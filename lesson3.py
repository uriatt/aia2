#могические методы в классах
# _add_(self+other)-сложение(+)
# _sub_(self+other)-вычитание(-)
# _mul_(self+other)-умножение(*)
# _floordiv(self+other)-целоечисло деление(//)
# _div_(self+other)-деленние(/)
# Множесественные наслодование
# what is inheritance?
# The diamond inheritance?
# The diamond inheritance problem
class Num:
    def __init__(self,num):
        self.num=num
    def _get_num(self):
        print(self.num)
    def __add__(self, other):
        print("It is Donder method__add__")
        self.num+=other
        self._get_num()
    def __sub__(self, other):
        print("It is Donder method __sub__")
        self.num=other

    def __mul__(self, other):

        print("It is Donder method__mul__")
        self.num*=other
        self._get_num()
    def __floordiv__(self, other):
        print("It is Donder method__floordiv__")
        self.num//=other
        self._get_num()
    def __truediv__(self, other):
        print("It is Donder method__truediv__")
        self.num/=other
        self._get_num()
num=Num(10)
#num.__add__(4)

#num+1
#num*10
#num.__mul__(10)
#num/10
#num.__truediv__(10)
#num//10
#num.__floordiv__(10)
class Num3(Num):
    pass
num1=Num3(10)
#num.__add__(10)
#class Num2(Num):
    pass
num2=Num2(20)
num2+1
# чем отличается магическая метод от другой
# магический метод вызывается определеный момент времени и определеные методами
#with -это постоянно с enter и exced (автоматически)
class Num3(Num):
    def __enter__(self):
        print("Enter")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
with Num3(30) as num:
    pass
