def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, '33g')
print_params(b = 25)
print_params(c = [1,2,3])
print()
values_list = [12.2, 'asdf', True]
values_dict = {'a': 12, 'b': 'string_', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = [54.32, 'Стр']
print_params(*values_list_2, 42)



