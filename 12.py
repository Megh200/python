
def rearrange_list_of_tuples(input_list):
    sorted_list = sorted(input_list, key=lambda x: (len(x), sum(x), min(x)))
    return sorted_list

def main():
    input_list = [tuple(map(int, input(f"Enter tuple {i + 1}: ").split(','))) for i in range(5)]

    result_list = rearrange_list_of_tuples(input_list)

    print("New List:", result_list)

if __name__ == "__main__":
    main()
