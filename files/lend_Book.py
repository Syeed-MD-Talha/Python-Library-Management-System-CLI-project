from files.colors import cl, clear_console
from files.file_operations import update_info
import time

def choose_option():
    print(f'{" "*32}🔄  {cl["c_177"]}{cl["bold"]}Press 1 to lend  book{cl["reset"]} ')
    time.sleep(0.2)
    print(f'{" "*32}🔄  {cl["c_177"]}{cl["bold"]}Press 2 to return book{cl["reset"]}')
    time.sleep(0.2)
    print(f'{" "*32}🔄  {cl["c_177"]}{cl["bold"]}Press 3 to LendBook details{cl["reset"]}')
    time.sleep(0.2)
    print(f'{" "*32}🔄  {cl["c_177"]}{cl["bold"]}Press # to exit{cl["reset"]}')
    time.sleep(0.2)
    return input(f'{" "*32}🎯 {cl["c_51"]}{cl["bold"]}Choose:{cl["reset"]}')

def lent_book(Books):
    name = input(f'{" "*32}{cl["bold"]}Enter your name:{cl["reset"]} ')
    while not name:
        print(f"{" "*32}{cl['c_1']}{cl['bold']}name can't be empty.🚫 {cl['reset']}")
        name = input(f'{" "*32}{cl["bold"]}Enter your name:{cl["reset"]} ')

    title = input(f'{" "*32}{cl['bold']}Enter the book name which you want to lend: {cl['reset']}').lower()
    book_found = False
    for book in Books:
        if book['title'].lower() == title:
            book_found = True
            if book['quantity'] > 0:
                print(f"{" "*32}'{book['title']}' is available.")
                book['quantity'] -= 1
                book['book_Borrowers'].append(name)
                book['is_lent'] = True
                clear_console()
                print(f"{" "*32}{cl['c_10']}{cl['bold']}Book lent successfully. ✅{cl['reset']} {cl['bold']}Remaining quantity:{cl['reset']} {cl['bold']}{cl['c_214']}{book['quantity']}{cl['reset']}\n")
                update_info(Books)
            else:
                print(f"{" "*32}{cl['c_197']}{cl['bold']}{cl['Italic']}'{book['title']}'{cl['reset']} {cl['c_197']}not enough books available to lend.{cl['reset']}")
            break
    
    if not book_found:
        print(f"{" "*32}{cl['c_1']}{cl['bold']}The book you requested is not available in the library.🚫 ⛔❗{cl['reset']}")
        # choose_option()

def return_book(Books):
    book_found = False
    username = input(f'{" "*32}{cl['bold']}Enter your user name:{cl['reset']} ')
    book_name = input(f'{" "*32}{cl['bold']}Enter the book name which you want to return:{cl['reset']} ')
    for book in Books:
        if book['title'].lower() == book_name.lower():
            if username not in book['book_Borrowers']:
                continue
            book_found = True
            book['quantity'] += 1
            book['book_Borrowers'].remove(username)
    
    if not book_found:
        print(f"{" "*32}{cl['c_1']}{cl['bold']}Sorry!!!{cl['reset']} {cl['c_196']}{cl['bold']}book title{cl['reset']}{cl['c_1']}{cl['bold']} or{cl['reset']} {cl['c_196']}{cl['bold']}username is not available.{cl['reset']} {cl['c_1']}{cl['bold']}please try again ⛔{cl['reset']}")
    else:
        print(f"{" "*32}{cl['c_10']}{cl['bold']}Successfully Done ✅ {cl['reset']}")
        update_info(Books)

def lent_book_details(Books):
    clear_console()
    print(f"\n{" "*30}{cl['c_51']}=================⭕ {cl['bold']}{cl['c_51']}List of the Books and Book Borrowers{cl['reset']} ⭕{cl['c_51']} ================\n{cl['reset']}")
    for book in Books:
        if len(book['book_Borrowers'][0]):
            print(f"{" "*30}📌 {cl['c_192']}{cl['bold']}{cl['Italic']}`{book['title']}`{cl['reset']} {cl['c_84']}was lent by: {cl['reset']}", end='')
            print(f"{cl['c_210']}{', '.join(book['book_Borrowers'])}{cl['reset']} ")
            time.sleep(0.4)
    print(f"{cl['c_51']}\n{" "*30}============================⭕ ⭕ ⭕ ⭕ ⭕===================================\n{cl['reset']}")

# Main function to tie everything together
def book_lending_system(Books):
    while True:
        option = choose_option()
        if option == '1':
            lent_book(Books)
        elif option == '2':
            return_book(Books)
        elif option == '3':
            lent_book_details(Books)
        elif option=='#':return
        else:
            print(f"{" "*32}{cl['c_196']}{cl['bold']}{cl['Italic']}Invalid option. Please try again.{cl['reset']}")
