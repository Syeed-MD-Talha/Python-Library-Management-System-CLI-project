import csv

# Data to be stored in the CSV file
Books = [
    {
        'title': 'Lord of the Rings: The Return of the King',
        'authors': ['Labib', 'Tolkien'],
        'isbn': '232343434',
        'year': '02-05-2005',
        'price': 50,
        'quantity': 3,
        'is_lent': True,
        'book_Borrowers': ['Sayed', 'Rozob', 'Talha']
    },
    {
        'title': 'Harry Potter',
        'authors': ['Rowling', 'Harry', 'Potter'],
        'isbn': '232343434',
        'year': '02-05-1999',
        'price': 500,
        'quantity': 100,
        'is_lent': True,
        'book_Borrowers': ['Babul', 'Abbas', 'Siam'],
    },
    {
        'title': 'The Hobbit',
        'authors': ['Tolkien', 'Harry'],
        'isbn': '123456789',
        'year': '21-09-1937',
        'price': 30,
        'quantity': 150,
        'is_lent': True,
        'book_Borrowers': ['Umair', 'Sayem']
    },
    {
        'title': 'Pride and Prejudice',
        'authors': ['Jane', 'Austen', 'Harry'],
        'isbn': '987654321',
        'year': '28-01-1813',
        'price': 25,
        'quantity': 80,
        'is_lent': True,
        'book_Borrowers': ['Polash', 'Ahsan'],
    },
    {
        'title': 'The fame of 1984',
        'authors': ['George', 'Orwell', 'Talha'],
        'isbn': '111222333',
        'year': '06-06-1949',
        'price': 35,
        'quantity': 120,
        'is_lent': True,
        'book_Borrowers': ['Adil']
    }
]

# File name
file_name = 'books_info.csv'

# Write data to CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['title', 'authors', 'isbn', 'year', 'price', 'quantity', 'is_lent', 'book_Borrowers'])
    
    # Write the data
    for book in Books:
        writer.writerow([
            book['title'],
            ','.join(book['authors']),
            book['isbn'],
            book['year'],
            book['price'],
            book['quantity'],
            book['is_lent'],
            ','.join(book['book_Borrowers'])
        ])

print(f"Data has been written to {file_name}")
