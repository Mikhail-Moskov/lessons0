def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(None,[1, 2],'String')
print_params(5, 5)
print_params(None)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [ False, 'String', 5]
value_dick = {'a' : None, 'b' : 2, 'c' : 'Home'}
print_params(*values_list)
print_params(**value_dick)
values_list_2 = [[1,2], False]
print_params(*values_list_2)
