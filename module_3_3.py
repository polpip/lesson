def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(b=25,c=[1,2,3])

values_list = (30,'python',True)
print_params(values_list)
values_list = (30,25,27)
values_dict = {"a":25,"b":23,"c":27}
values_dict = {"a":values_list[0],"b":values_list[1],"c":values_list[2]}
print_params(**values_dict)
