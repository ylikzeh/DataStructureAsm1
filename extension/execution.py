import time
from extension.excel_utility import import_books_from_excel, write_books_to_matrix
from extension.radix_sort import radix_sort

def sort_books_and_measure_time(books):
    compare_time = 0.0
    move_time = 0.0
    compare_count = 0
    move_count = 0
    compare_milestones = {}
    move_milestones = {}
    all_compare_times = []
    all_move_times = []
    start_time = time.time()
    start_sort_time = start_time  

    compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times = radix_sort(
        books, compare_time, move_time, compare_count, move_count, compare_milestones, move_milestones, all_compare_times, all_move_times, start_sort_time
    )

    sort_time = time.time() - start_time
    return compare_time, move_time, sort_time, compare_milestones, move_milestones, all_compare_times, all_move_times, compare_count, move_count

def test_import_and_sort(file_path, execution_time_log_sorted,dataset_size):
    books = import_books_from_excel(file_path)
    if dataset_size==100:
        write_books_to_matrix(books,False)
    compare_time, move_time, sort_time, compare_milestones, move_milestones, all_compare_times, all_move_times, compare_count, move_count = sort_books_and_measure_time(books)

    print(f"Execution Time Summary for datasize of {dataset_size} data:")
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
        log_file.write(f"Execution Time Summary for datasize of {dataset_size} data: \n")
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
