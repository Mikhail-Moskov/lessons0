my_dict = {'Mikhail': 1989, 'Miron': 2020, 'Alex': 1970}
print (my_dict)
print (my_dict['Mikhail'])
print (my_dict.get('Anna', 1994))
my_dict.update({'Inna': 1968,
                'Yula': 1975})
print (my_dict.pop('Miron'))
print (my_dict)
my_set = {1, 1, 2, 2, 2, 'Anna','Anna', (1, 2)}
print (my_set)
my_set.add('Miron')
my_set.add(3)
my_set.remove(1)
print(my_set)