immutable_var = 1, 'Word', False, [0, 1, 2, 3]
print (immutable_var)
immutable_var[3][0] = 3
print (immutable_var)
mutable_list = [0, 1, 2, 3]
mutable_list.append(int(input('Введите цифру: ')))
mutable_list[0] = mutable_list [4]
print (mutable_list)
