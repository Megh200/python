
def create_set(search_query):
    search_results = list(search(search_query, num=10, stop=10, pause=2))
    url_list = [result.split('//')[1].split('/')[0] for result in search_results]
    result_set = set(item[:4] for item in url_list)
    return result_set

def main():
    user_input = input("Enter a search query to Google: ")

    result_set = create_set(user_input)

    print("Result Set:", result_set)

if __name__ == "__main__":
    main()


