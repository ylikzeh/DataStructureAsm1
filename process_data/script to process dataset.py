import csv
import chardet
import pandas as pd

def extract_book_data_from_csv(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            result = chardet.detect(f.read())
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")

        extracted_data = []
        with open(input_file, 'r', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for i, row in enumerate(reader):
                try:
                    # Split the row into 5 columns, discarding any extra data
                    extracted_row = row[:5]
                    res = ' '.join(extracted_row).replace("\"","")
                    extracted_row=res.split(";")
                    # Pad with empty strings if necessary
                    extracted_row = extracted_row[:5]
                    extracted_data.append(extracted_row)

                except IndexError:
                    print(f"Row {i+1} has an error: {row}")
                    continue

        df = pd.DataFrame(extracted_data, columns=['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher'])
        df.to_excel(output_file, index=False)
        print(f"Data successfully extracted and saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_csv_file = "books.csv"  # Replace with your actual input file path
output_excel_file = "data.xlsx"
extract_book_data_from_csv(input_csv_file, output_excel_file)