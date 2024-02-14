# lnbregister.py
import csv
from datetime import datetime

def is_valid_id(id):
    return len(id) == 10 and id[:5].isalpha() and id[5:].isdigit()

def is_valid_dob(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    # User input to create a CSV file
    with open('lnbregister.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Amount', 'DOB']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'ID': 'ABCDE12345', 'Amount': 100, 'DOB': '1990-01-01'})
        writer.writerow({'ID': 'ABCDE54321', 'Amount': 150, 'DOB': '1995-02-15'})
        writer.writerow({'ID': 'FGHIJ98765', 'Amount': 200, 'DOB': '2000-05-20'})
        writer.writerow({'ID': 'FGHIJ98765', 'Amount': 250, 'DOB': '2000-05-20'})
        writer.writerow({'ID': 'KLMNO24680', 'Amount': 300, 'DOB': '1988-12-31'})

    # Import the CSV file and perform validation
    with open('lnbregister.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Verification']

        # Write to a new CSV file
        with open('lnbregister_verified.csv', 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if is_valid_id(row['ID']) and is_valid_dob(row['DOB']):
                    row['Verification'] = 'Verified'
                    writer.writerow(row)
                else:
                    row['Verification'] = 'Invalid'
                    writer.writerow(row)

if __name__ == "__main__":
    main()
