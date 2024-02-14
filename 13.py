
def words_more_than_four_letters(input_string):
    words = input_string.split()
    result_list = [word for word in words if len(word) > 4]
    return result_list

def main():
    input_string = input("Enter a sentence or paragraph: ")

    result_list = words_more_than_four_letters(input_string)

    print("Result List:", result_list)

if __name__ == "__main__":
    main()
