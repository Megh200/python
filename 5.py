# lnbattendance.py

def max_consecutive_days(e, w, data):
    max_consecutive = 0
    current_consecutive = 0

    for day in range(w):
        all_present = all(data[i][day] == 'P' for i in range(e))

        if all_present:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0

    return max_consecutive

def main():
    e = 5
    w = 7
    data = [
        "PPPPP",
        "PPAPP",
        "AAAPP",
        "PAPAP",
        "AAAAA",
        "PAAAP",
        "PPPPP"
    ]

    result = max_consecutive_days(e, w, data)
    print(f"The maximum number of consecutive days with all employees present is: {result}")

if __name__ == "__main__":
    main()
