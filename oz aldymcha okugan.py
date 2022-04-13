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