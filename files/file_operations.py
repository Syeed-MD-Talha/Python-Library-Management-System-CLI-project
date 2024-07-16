
import csv
file_name = 'books_info.csv'

def update_info(Books):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'authors', 'isbn', 'year', 'price', 'quantity', 'is_lent', 'book_Borrowers'])
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
    # print(f"Data has been written to {file_name} Successfully ✅✅✅")

def fetchData_from_file():
    Book=[]
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader) # here i just skip the title
        for row in reader:
            book = {
                'title': row[0],
                'authors': row[1].split(','),
                'isbn': row[2],
                'year': row[3],
                'price': float(row[4]),
                'quantity': int(row[5]),
                'is_lent': row[6] == 'True',
                'book_Borrowers': row[7].split(',')
            }
            Book.append(book)
        return Book
