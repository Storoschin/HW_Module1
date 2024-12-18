#Работа со словарём
my_dict = {'Alex':1987,'Den':1989, 'Tom':2000, 'Bob':1995}
print(my_dict)
print(my_dict['Bob'])
print(my_dict.get('Andrew','Такого ключа нет'))
my_dict.update({'Katrin':1990, 'Valery':1997})
a=my_dict.pop('Tom')
print(a)
print(my_dict)

#Работа со множествами
my_set = {1,3,4, 10, 11, 12,'str1', 3,4, 10, 'str1', (10,20,30)}
print(my_set)
my_set.add('new_str')
my_set.add((33,True,21))
my_set.discard((10,20,30))
print(my_set)