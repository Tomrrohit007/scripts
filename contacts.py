import pandas as pd
import re
from tkinter import Tk, filedialog
import random

def generate_random_digits():
    return ''.join(str(random.randint(0, 9)) for _ in range(5))

def change_last_five_digits(phone_number):
    if pd.notna(phone_number):
        digits = re.findall(r'\d', str(phone_number))
        if len(digits) >= 5:
            digits[-5:] = list(generate_random_digits())
            return ''.join(digits)
    return phone_number

def process_contacts(input_file_path, output_file_path):
    contacts_df = pd.read_csv(input_file_path)

    phone_columns = ["Phone 1 - Value", "Phone 2 - Value", "Phone 3 - Value"]
    
    for column in phone_columns:
        if column in contacts_df.columns:
            contacts_df[column] = contacts_df[column].apply(change_last_five_digits)

    contacts_df.to_csv(output_file_path, index=False)

def main():
    # Prompt user to select input file
    Tk().withdraw()  # prevent root window from appearing
    input_file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

    if not input_file_path:
        print("No file selected. Exiting.")
        return

    # Create output file path
    output_file_path = input_file_path.replace('.csv', '-copy.csv')

    # Process contacts and save to the new file
    process_contacts(input_file_path, output_file_path)

    print(f"Contacts processed and saved to: {output_file_path}")

if __name__ == "__main__":
    main()
