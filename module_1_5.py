immutable_var = (1,2,3,4,[1,2,3], "true")
print(immutable_var)
#immutable_var[3][0] = картеж не изменяем
immutable_var[4][0] = 5
mutable_list = [1,2,3,4,"true"]
print(mutable_list)
mutable_list[3] = 500
print(mutable_list)