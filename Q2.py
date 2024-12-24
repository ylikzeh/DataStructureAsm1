from execution import test_import_and_sort
from excel_utility import write_sorted_books_to_file

# Main function to ask user for input
def main():
    while True:
        print("Which Excel file would you like to sort?")
        print("1. Excel with sorted book data")
        print("2. Excel with nearly sorted book data")
        print("0. Exit")
        choice = input("Enter 1, 2, or 0 to exit: ")

        if choice == '1':
            file_path = "data_sorted.xlsx"  # Replace with the actual path for Excel A
            execution_time_log_path = 'SA2_execution_time_log_sorted.txt'
            sorted_data_path = 'SA2_sorted_book_data_sorted.txt'
            break
        elif choice == '2':
            file_path = 'data_sorted.xlsx'  # Replace with the actual path for Excel B
            execution_time_log_path = 'SA2_execution_time_log_nearly_sorted.txt'
            sorted_data_path = 'SA2_sorted_book_data_nearly_sorted.txt'
            break
        elif choice == '0':
            print("Exiting the program.")
            return  # Exit the function and program
        else:
            print("Invalid choice. Please enter 1, 2, or 0 to exit.")

    # Once the user selects a valid option, call the sorting function
    books = test_import_and_sort(file_path, execution_time_log_path)
    if books:
        print(f"Execution time for compare and move operation has been written to {execution_time_log_path}")
        write_sorted_books_to_file(books, sorted_data_path)  # Write sorted books to file
    else:
        print("No books were sorted. Please check the input file.")

    main()

if __name__ == '__main__':
    main()
