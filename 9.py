def is_cat_and_dog_equal(input_str):
    return input_str.lower().count('cat') == input_str.lower().count('dog')

user_input = input("Enter a string: ")

result = is_cat_and_dog_equal(user_input)
print(result)
