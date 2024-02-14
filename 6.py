def convert_to_binary_tuples(numbers):
    binary_tuples = tuple(bin(num) for num in numbers)
    return binary_tuples

def main():
    input_numbers = []
    for i in range(20):
            number = int(input(f"Enter integer {i + 1}: "))
            input_numbers.append(number)
    binary_tuples = convert_to_binary_tuples(input_numbers)

    last_two_tuples = binary_tuples[-2:]
    print("Binary Tuples:", last_two_tuples)
    
    result_and = bin(int(last_two_tuples[0], 2) & int(last_two_tuples[1], 2))
    result_or = bin(int(last_two_tuples[0], 2) | int(last_two_tuples[1], 2))
    
    print("Result of AND as Integer:", int(result_and, 2))
    print("Result of OR as Integer:", int(result_or, 2))

if __name__ == "__main__":
    main()



