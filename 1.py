
print('enter ')
def main():
    numbers = [int(input()) for i in range(5)]
    ans = [num for num in numbers if num > 9]
    print(ans)
if __name__ == "__main__":
    main()


