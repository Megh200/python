# lnbbreaktuple.py

def break_tuple(input_tuple):
    sorted_tuple = tuple(sorted(input_tuple))
    mid = len(sorted_tuple) // 2

    first_part = sorted_tuple[:mid]
    second_part = sorted_tuple[mid:]

    return first_part, second_part

def main():
    input_tuple = tuple(map(int, input("Enter a tuple of numeric values (at least 3 values): ").split(',')))

    if len(input_tuple) < 3:
        print("Please enter at least 3 numeric values.")
        return

    result_tuple1, result_tuple2 = break_tuple(input_tuple)

    print("Result Tuple 1:", result_tuple1)
    print("Result Tuple 2:", result_tuple2)

if __name__ == "__main__":
    main()
