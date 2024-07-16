from files.colors import cl,clear_console
from files.file_operations import update_info
import time

def remove_book(Books):
    ids=[]
    clear_console()
    not_found=True
    title=input(f'{" "*50}{cl['c_84']}{cl['bold']}Enter book title:{cl['reset']}')
    for index,book in enumerate(Books):
        if title.lower() in book["title"].lower():
            ids.append(index)
            not_found=False
            print(f"{" "*50}{cl['c_87']}{cl['bold']}id:{cl['reset']}{cl['bold']}{cl['c_226']}{index+1}{cl['reset']} and book name: {cl['c_11']}{cl['Italic']}{book['title']}{cl['reset']}")
    
    if not_found:
        print(f'{" "*50}{cl['c_198']}{cl['bold']}No book found for this title. please try again 👻{cl['reset']}')
        time.sleep(1)
        # remove_book(Books)
    else:
        id=input(f'{" "*50}{cl['bold']}Select {cl['c_87']}id{cl['reset']} {cl['bold']}to delete❌ the book or press {cl['c_196']}{cl['bold']}q{cl['reset']} to quit:{cl['reset']}')
        if id=='q':
            clear_console()
            return
        id=int(id)-1
        while id not in ids:
            print(f'{" "*50}{cl['c_198']}{cl['bold']}Invalid input please select displaying id only{cl['reset']}')
            id=input(f'{" "*50}{cl['bold']}Select {cl['c_87']}id{cl['reset']} {cl['bold']}to delete❌ the book or press {cl['c_196']}{cl['bold']}q{cl['reset']} to quit:{cl['reset']}')
            if id=='q':
                clear_console()
                return
            id=int(id)-1



        Books.pop(id)  
        clear_console()
        time.sleep(0.7)
        print(f'\n{" "*50}{cl['c_83']}{cl['bold']}Book has removed successfully ✅{cl['reset']}')
        update_info(Books)