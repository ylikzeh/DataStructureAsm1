from extension.excel_utility import write_books_to_matrix, write_sorted_books_to_file
from extension.execution import test_import_and_sort

# Main function to ask user for input
def main():
    while True:
        print("Which Excel file would you like to sort?")
        print("1. Excel with 100 row of random book data")
        print("2. Excel with 100 row nearly sorted book data")
        print("3. Excel with 500 row of random book data")
        print("4. Excel with 500 row nearly sorted book data")
        print("5. Excel with 1000 row of random book data")
        print("6. Excel with 1000 row nearly sorted book data")
        print("0. Exit")
        choice = input("Enter 1 to 6 or 0 to exit: ")
        dataset_size = 0
        if choice == '1':
            file_path = 'data_random/data_random_100.xlsx'
            execution_time_log_path = 'Q2 result/SA2_execution_time_log_random.txt'
            sorted_data_path = 'Q2 result/SA2_sorted_book_data_random.txt'
            dataset_size = 100
            break
        elif choice == '2':
            file_path = 'data_nearly_sorted/data_nearly_sorted_100.xlsx' 
            execution_time_log_path = 'Q2 result/SA2_execution_time_log_nearly_sorted.txt'
            sorted_data_path = 'Q2 result/SA2_sorted_book_data_nearly_sorted.txt'
            dataset_size = 100
            break
        elif choice == '3':
            file_path = 'data_random/data_random_500.xlsx'
            execution_time_log_path = 'Q2 result/SA2_execution_time_log_random.txt'
            sorted_data_path = 'Q2 result/SA2_sorted_book_data_random.txt'
            dataset_size = 500
            break
        elif choice == '4':
            file_path = 'data_nearly_sorted/data_nearly_sorted_500.xlsx'  
            execution_time_log_path = 'Q2 result/SA2_execution_time_log_nearly_sorted.txt'
            sorted_data_path = 'Q2 result/SA2_sorted_book_data_nearly_sorted.txt'
            dataset_size = 500
            break
        elif choice == '5':
            file_path = 'data_random/data_random_1000.xlsx'
            execution_time_log_path = 'Q2 result/SA2_execution_time_log_random.txt'
            sorted_data_path = 'Q2 result/SA2_sorted_book_data_random.txt'
            dataset_size = 1000
            break
        elif choice == '6':
            file_path = 'data_nearly_sorted/data_nearly_sorted_1000.xlsx'
            execution_time_log_path = 'Q2 result/SA2_execution_time_log_nearly_sorted.txt'
            sorted_data_path = 'Q2 result/SA2_sorted_book_data_nearly_sorted.txt'
            dataset_size = 1000
            break
        elif choice == '0':
            print("Exiting the program.")
            return  # Exit the function and program
        else:
            print("Invalid choice. Please enter 1 to 6 or 0 to exit.")

    # Once the user selects a valid option, call the sorting function
    books = test_import_and_sort(file_path, execution_time_log_path, dataset_size)
    print(f"Execution time for compare and move operation has been written to {execution_time_log_path}")
    if dataset_size==100:
        write_books_to_matrix(books, True)
    write_sorted_books_to_file(books, sorted_data_path)  # Write sorted books to file

    main()

if __name__ == '__main__':
    main()
