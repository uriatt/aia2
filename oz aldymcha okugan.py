#urok .мНОЖЕСТВО
#number={1,2,3,4,5,6,78}
#print(number)
# numbers=set([1,1,2,2,3,4,4,5,5,6])
# print(numbers)
numbers={1,2,3,4,5,6}
# for i in numbers:
#     print(i)
# print(9 in numbers)
# numbers.add(45)#добавить
# print(numbers)
# numbers.pop()#удалить постояно первый элемент
# numbers.discard(45)#удалить
# numbers.remove(3)
# numbers.clear()#удалить все элементы
# print(numbers)#уалить
numbers2={3,4,5,7,1,2}
#numbers3=numbers.union(numbers2)#обединяеть|
#numbers3=numbers-numbers2#экоондо жокторду чыгарат .биринчи эмнени жазган болсок
#numbers3=numbers.intersection(numbers2)#экоондо барларды гана чыгарать&
numbers3=numbers2.copy()
print(numbers3)
print(len(numbers2))#канча элемент бар экендигин корсотот
numbers4=frozenset({2,3,5,6,78,8})с помошю метода замороско мы не сможем изменить
numbers4.add(3)
print(numbers4)
####
>>> x = Fraction(2, 5)
>>> y = Fraction(3, 7)
>>>
>>> x + y, y - x
(Fraction(29, 35), Fraction(1, 35))
>>>
>>> x*y, x/y
(Fraction(6, 35), Fraction(14, 15))
>>>
>>> x**0.5, 2**0.5/5**0.5
(0.6324555320336759, 0.6324555320336759)
>>>
>>> x**y, (x**3)**(1/7)
(0.6752339686501552, 0.6752339686501552)
>>>
>>> y//x
1
>>> x%y
Fraction(2, 5)