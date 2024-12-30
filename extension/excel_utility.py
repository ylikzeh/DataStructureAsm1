import pandas as pd
from extension.book import Book 

# Function to import data from Excel
def import_books_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        books = []
        for _, row in df.iterrows():
            books.append(Book(row['ISBN'], row['Book-Title'], row['Book-Author'], row['Year-Of-Publication'], row['Publisher']))
        return books
    except Exception as e:
        print(f"Error importing books: {e}")
        return []

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


def write_books_to_matrix(books,status):
    counter = 1
    print ("---------------------------------")
    if status:
        print ("Sorted book matrix :")
    else:
        print ("Unsorted book matrix :")
    
    for book in books:
        print(f"{book.isbn:<10}", end=' ') 
        
        if counter%10==0 and counter!=0:
            print()
        counter += 1
    print ("---------------------------------")