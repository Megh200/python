original_list = list(range(1, 21))
new_list = original_list[:5] + original_list[-5:]

print("New List:", new_list)

squared_list = [num ** 2 for num in new_list]
print("Squared List:", squared_list)

split_parts = [new_list[:2], new_list[2:5], new_list[5:]]
print("Split Parts:", split_parts)
