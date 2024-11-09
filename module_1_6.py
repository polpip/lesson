my_dict = {'Anna':1975, 'Adam':1990, 'Tom':1993}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Alisa'))
my_dict.update({'Nina':1991,'Sasha':1995})
print(my_dict.pop('Tom'))
print(my_dict)
my_set = [1,1,1,2,2,2,3,3,4,4,5,5,6,'Person']
my_set = set(my_set)
my_set.remove(2)
my_set.add('apple')
my_set.add('coconut')
print(my_set)
