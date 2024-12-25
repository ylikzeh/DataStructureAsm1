import time
import pandas as pd

# Book class definition
class Book:
    def __init__(self, isbn, name, author, year, publisher):
        self.isbn = isbn  # ISBN is a string
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher

    def __repr__(self):
        return f"Book(ISBN: {self.isbn}, Name: {self.name})"

# Function to import data from Excel
def import_books_from_excel(file_path):
    df = pd.read_excel(file_path)  # Reading Excel data into a DataFrame
    books = []
    for _, row in df.iterrows():
        books.append(Book(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['Publisher']))
    return books

# Quick Sort Algorithm with special time tracking
def quick_sort(arr, low, high, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time):
    if low < high:
        # The 'partition' operation is where comparisons and moves happen
        pi, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = partition(
            arr, low, high, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
        )

        # Recursively apply quick sort to the subarrays (left of the pivot and right of the pivot)
        compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = quick_sort(
            arr, low, pi - 1, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
        )  # Left subarray
        compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = quick_sort(
            arr, pi + 1, high, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
        )  # Right subarray

    return compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times

# Partition function with milestone tracking
def partition(arr, low, high, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time):
    # Median of three pivot selection
    first = arr[low]  # First element
    middle = arr[(low + high) // 2]  # Middle element
    last = arr[high]  # Last element

    # Compare the first, middle, and last elements to find the median
    pivot_candidate = sorted([first.isbn, middle.isbn, last.isbn])[1]

    # Choose the pivot as the median of the three
    if pivot_candidate == first.isbn:
        pivot = arr[low]
    elif pivot_candidate == middle.isbn:
        pivot = arr[(low + high) // 2]
    else:
        pivot = arr[high]
        
    pivot = next(book for book in [first, middle, last] if book.isbn == pivot_candidate)
    pivot_index = arr.index(pivot)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1  # Initializing the partition index

    # Compare each element with the pivot (Comparison Operation)
    for j in range(low, high):
        start_compare_time = time.time()  # Start timing the comparison
        
        # Perform the comparison
        is_less_than_pivot = arr[j].isbn < pivot.isbn
        
        # Add time for the comparison (true or false)
        compare_time += time.time() - start_compare_time  # Add the comparison time to total compare time
        all_compare_times.append(time.time() - start_compare_time)  # Track individual comparison times
        compare_count += 1  # Increment comparison count

        # Check if we've reached a milestone (100, 500, 1000 comparisons)
        check_milestone(compare_count, compare_milestones, start_sort_time)


        if is_less_than_pivot:
            # Swap operation (Move Operation)
            start_move_time = time.time()  # Start timing the move (swap)
            i += 1  # Move the partition index to the right
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements
            move_time += time.time() - start_move_time  # Add the move time to total move time
            all_move_times.append(time.time() - start_move_time)  # Track individual move times
            move_count += 1  # Increment move count

            # Check if we've reached a milestone (100, 500, 1000 moves)
            check_milestone(move_count, move_milestones, start_sort_time)

    # Final swap operation: Place the pivot element in the correct position
    start_move_time = time.time()  # Start timing the final swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to its correct position
    move_time += time.time() - start_move_time  # Add the move time for this final swap
    all_move_times.append(time.time() - start_move_time)  # Track individual move times
    move_count += 1  # Increment move count

    # Check if we've reached a milestone (100, 500, 1000 moves)
    check_milestone(move_count, move_milestones, start_sort_time)

    return i + 1, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times

def check_milestone(count, milestones_dict, start_sort_time):
    milestones = [100, 500, 1000]
    for milestone in milestones:
        if count >= milestone and milestone not in milestones_dict:
            # Use 'operation' to modify the correct milestone dictionary
            milestones_dict[milestone] = time.time() - start_sort_time  # Relative time since sorting started

# Helper function to measure the total time
def sort_books_and_measure_time(books):
    compare_time = 0.0
    move_time = 0.0
    compare_count = 0
    move_count = 0
    compare_milestones = {}  # Separate dictionary for comparison milestones
    move_milestones = {}  # Separate dictionary for move milestones
    all_compare_times = []  # List to track compare times for all elements
    all_move_times = []  # List to track move times for all elements
    start_time = time.time()
    start_sort_time = start_time  # Base time for milestone tracking

    compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = quick_sort(
        books, 0, len(books) - 1, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
    )

    sort_time = time.time() - start_time
    return compare_time, move_time, sort_time, compare_milestones, move_milestones, all_compare_times, all_move_times, compare_count, move_count

# Main function to sort and log results
def test_import_and_sort(file_path, execution_time_log_sorted):
    books = import_books_from_excel(file_path)

    compare_time, move_time, sort_time, compare_milestones, move_milestones, all_compare_times, all_move_times, compare_count, move_count = sort_books_and_measure_time(books)

    print(f"Total Comparisons: {compare_count}")
    print(f"Total Moves: {move_count}")
    
    print(f"Total Comparison Time: {compare_time:.6f} seconds")
    print(f"Total Move Time: {move_time:.6f} seconds")
    print(f"Total Sorting Time: {sort_time:.6f} seconds")

    print("\nComparison time for N data:")
    for milestone, milestone_time in compare_milestones.items():
        print(f"    Time for {milestone} comparisons: {milestone_time:.6f} seconds")

    print("\nMove/Swap time for N data:")
    for milestone, milestone_time in move_milestones.items():
        print(f"    Time for {milestone} moves: {milestone_time:.6f} seconds")

    with open(execution_time_log_sorted, "a+") as log_file:
        log_file.write(f"Total Comparisons: {compare_count}\n")
        log_file.write(f"Total Moves: {move_count}\n")
        
        log_file.write(f"Total Comparison Time: {compare_time:.6f} seconds\n")
        log_file.write(f"Total Move Time: {move_time:.6f} seconds\n")
        log_file.write(f"Total Sorting Time: {sort_time:.6f} seconds\n\n")

        log_file.write("Comparison time for N data:\n")
        for milestone, milestone_time in compare_milestones.items():
            log_file.write(f"   Time for {milestone} comparisons: {milestone_time:.6f} seconds\n")

        log_file.write("Move/Swap time for N data:\n")
        for milestone, milestone_time in move_milestones.items():
            log_file.write(f"   Time for {milestone} moves: {milestone_time:.6f} seconds\n")

        log_file.write("--------------------------------\n")

    return books    

# Function to write sorted books to a file
def write_sorted_books_to_file(books, sorted_data_path):
    counter = 1
    with open(sorted_data_path, "w+") as f:
        for book in books:
            f.write(f"Book Number : {counter}\n")
            f.write(f"Book ISBN : {book.isbn}\n")
            f.write(f"Book Title: {book.name}\n")
            f.write(f"Book Author: {book.author}\n")
            f.write(f"Publish  Year: {book.year}\n")
            f.write(f"Book Publisher: {book.publisher}\n")
            f.write("---------------------------------\n")
            counter += 1
    print(f"Sorted books have been written to {sorted_data_path}")

# Main function to ask user for input
def main():
    while True:
        print("Which Excel file would you like to sort?")
        print("1. Excel with random book data")
        print("2. Excel with nearly sorted book data")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            file_path = "data_random.xlsx"  # Replace with the actual path for Excel A
            execution_time_log_path = 'SA1_execution_time_log_random.txt'
            sorted_data_path = 'SA1_sorted_book_data_random.txt'
            break
        elif choice == '2':
            file_path = 'data_nearly_sorted.xlsx'  # Replace with the actual path for Excel B
            execution_time_log_path = 'SA1_execution_time_log_nearly_sorted.txt'
            sorted_data_path = 'SA1_sorted_book_data_nearly_sorted.txt'
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    # Once the user selects a valid option, call the sorting function
    books = test_import_and_sort(file_path, execution_time_log_path)
    print(f"Execution time for compare and move operation has been written to {execution_time_log_path}")
    write_sorted_books_to_file(books, sorted_data_path)  # Write sorted books to file

if __name__ == '__main__':
    main()
