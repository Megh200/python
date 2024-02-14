def main():
    num1 = int(input("first integer: "))
    num2 = int(input("second integer: "))
    product = num1 * num2
    print("Product:", product)
    if product > 500:
        total_sum = num1 + num2
        print("Sum ", total_sum)
    else:
        print("Hello LNB code is running fine !!")

if __name__ == "__main__":
    main()
