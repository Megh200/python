input_tuple = eval(input("Enter a tuple: "))
input_string = input("Enter a string: ")

list_from_tuple = list(input_tuple)

for i in range(len(list_from_tuple) * 2 - 1, 0, -2):
    list_from_tuple.insert(i, input_string)

tuple_result = tuple(list_from_tuple)

print(tuple_result)
