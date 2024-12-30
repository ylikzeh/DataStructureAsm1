import time
from extension.book import Book

# Function to check and record milestone
def check_milestone(count, milestones_dict, start_sort_time):
    milestones = [100, 500, 1000]
    for milestone in milestones:
        if count >= milestone and milestone not in milestones_dict:
            milestones_dict[milestone] = time.time() - start_sort_time  # Record the relative time when the milestone is reached

# Radix Sort Algorithm with special time tracking and milestone checking
def radix_sort(arr, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time):
    max_isbn_length = max(len(book.isbn) for book in arr)  # Find the maximum length of ISBNs
    for digit_pos in range(max_isbn_length):  # Process each digit position (from least significant to most significant)
        # Stable counting sort for the current digit
        arr, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = counting_sort_on_digit(
            arr, digit_pos, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
        )
    return compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times

# Counting Sort for a specific digit with milestone tracking
def counting_sort_on_digit(arr, digit_pos, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time):
    # Create 10 buckets for digits 0-9
    buckets = [[] for _ in range(10)]
    
    # Track the comparison timing for each element in the current iteration
    start_compare_time = time.time()

    for book in arr:
        # Get the character at the current digit position
        digit_char = book.isbn[-(digit_pos + 1)]  # Get the character at the specified position
        
        compare_count += 1  # Increment the comparison count for each comparison
        check_milestone(compare_count, compare_milestones, start_sort_time)  # Check for comparison milestone
        
        if digit_char.isdigit():
            digit = int(digit_char)  # Convert to integer if it's a digit
        elif digit_char == 'X' and digit_pos == 0:  # Handle 'X' in the last position (for ISBN-10)
            digit = 10  # 'X' represents 10 in ISBN-10
        else:
            continue  # Skip this book if it's not a valid ISBN character for this position
        
        # Ensure that the digit is within the range [0, 9] for valid buckets
        if digit == 10:  # Special handling for 'X' case
            digit = 9  # Place 'X' in the last bucket (index 9)
        
        # Ensure that the digit is between 0 and 9
        if 0 <= digit <= 9:
            buckets[digit].append(book)  # Move the book into the appropriate bucket
        else:
            print(f"Invalid digit encountered: {digit} for ISBN {book.isbn}")
            continue  # Skip this book if digit is out of range (unexpected case)
    
    # Track the comparison time for the current iteration
    compare_time += time.time() - start_compare_time  # Add the total comparison time for this digit iteration
    all_compare_times.append(time.time() - start_compare_time)  # Track individual compare times

    # Rebuild the list based on the sorted buckets
    start_move_time = time.time()  # Start timing the move
    
    index = 0
    for bucket in buckets:
        for book in bucket:
            arr[index] = book  # Rebuilding the array by placing books back into it
            index += 1
            move_count += 1  # Increment move count for each book moved to the array
            check_milestone(move_count, move_milestones, start_sort_time)  # Check for move milestone

    # Track the move time for this pass
    move_time += time.time() - start_move_time  # Add the move time for this pass
    all_move_times.append(time.time() - start_move_time)  # Track individual move times

    return arr, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times

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

    compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = radix_sort(
        books, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
    )

    sort_time = time.time() - start_time
    return compare_time, move_time, sort_time, compare_milestones, move_milestones, all_compare_times, all_move_times, compare_count, move_count
