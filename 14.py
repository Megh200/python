
def merge_lists_into_dict(list1, list2):
    result_dict = dict(zip(list1, list2))
    return result_dict

def main():
    list1 = input("Enter unique elements for the first list (separated by commas): ").split(',')
    list2 = input("Enter elements for the second list (same size as the first list, separated by commas): ").split(',')

    result_dict = merge_lists_into_dict(list1, list2)

    print("Result Dictionary:", result_dict)

if __name__ == "__main__":
    main()
