def main():
    str = input("Enter a string: ")

    length = len(str)
    print("Length of the string:", length)
    if length > 7:
        even = str[::2]
        print("Characters at even indices:", even)
    else:
        odd = str[1::2]
        print("Characters at odd indices:", odd)

if __name__ == "__main__":
    main()
