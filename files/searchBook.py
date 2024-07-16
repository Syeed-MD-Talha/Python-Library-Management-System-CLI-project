from files.colors import cl,clear_console
import time

# Colors and styles
Italic= "\033[3m"
reset = "\033[0m"
bold = "\033[1m"
underline = "\033[4m"
blue = "\033[94m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[96m"
red = "\033[91m"
magenta = "\033[35m"
bright_magenta = "\033[95m"

def display(book):
        print(f'{" "*32}{bold}{bright_magenta}{"="*30} 📖 {bold}{cl['c_226']}{Italic}{book["title"]}  {magenta}{"="*30}{reset}')
        print(f'{" "*32}📝 {bold}Title:{reset}           {Italic}{bold}{yellow}"{book["title"]}"{reset}')
        print(f'{" "*32}✍️  {bold}Authors:{reset}         {blue}{", ".join(book["authors"])}{reset}')
        print(f'{" "*32}📕 {bold}ISBN:{reset}            {magenta}{book["isbn"]}{reset}')
        print(f'{" "*32}📅 {bold}Publishing Year:{reset} {red}{book["year"]}{reset}')
        print(f'{" "*32}💰 {bold}Price:{reset}           {cyan}${book["price"]:.2f}{reset}')
        print(f'{" "*32}🔢 {bold}Quantity:{reset}        {book["quantity"]}{reset}')
        print(f'{" "*32}{bold}{magenta}{"="*75}{reset}\n')
        time.sleep(0.7)



def search_book(Books):
    print(f'\n{" "*32}🔸 🔸 🔸 🔸 🔸 🔸   {bold}{cl['c_87']}choose any option:{reset}  🔸 🔸 🔸 🔸 🔸')
    print(f'{" "*32}{cl['bold']}{cl['c_49']}1.{cl['reset']} {cl['c_184']}Search by title{cl['reset']}')
    print(f'{" "*32}{cl['bold']}{cl['c_49']}2.{cl['reset']} {cl['c_184']}Search by ISBN{cl['reset']}')
    print(f'{" "*32}{cl['bold']}{cl['c_49']}3.{cl['reset']} {cl['c_184']}Search by author{cl['reset']}')
    print(f'{" "*32}{cl['bold']}{cl['c_49']}4.{cl['reset']} {cl['c_196']}{cl['bold']}Exit{cl['reset']} {cl['c_184']}this menu{cl['reset']}\n')
    option=input(f'{" "*32}🎯 {bold}{cl['c_87']}choose:{cl['reset']} ')
    if option=='1':
        clear_console()
        not_found=True
        title=input(f"\n{" "*30}{cl['bold']}{cl['c_87']}Enter book title:{cl['reset']} ")
        while not title:
            print(f"{" "*32}{cl['c_196']}Title can't be empty{cl['reset']}")
            title=input(f"{" "*32}{cl['bold']}Enter book title:{cl['reset']}")
        for book in Books:
            if title.lower() in  book['title'].lower():
                not_found=False
                display(book)
        if not_found:
            clear_console()
            time.sleep(0.5)
            print(f'\n{" "*30}{cl['bold']}{cl['c_196']}No book found for this title❗❗❗{cl['reset']}')
        search_book(Books)
    elif option=='2':
        clear_console()
        not_found=True
        isbn=input(f"{" "*32}{cl['bold']}{cl['c_87']}Enter ISBN:{cl['reset']} ")
        while not isbn:
            print(f"{" "*32}{cl['c_196']}ISBN can't be empty{cl['reset']}")
            isbn=input(f"{" "*32}{cl['bold']}Enter ISBN:{cl['reset']}")
        for index,book in enumerate(Books):
            if isbn.lower() in  book['isbn'].lower():
                not_found=False
                display(book)
        if not_found:
            clear_console()
            time.sleep(0.5)
            print(f'\n{" "*30}{cl['bold']}{cl['c_196']}No book found for this ISBN❗❗❗{cl['reset']}')
            #search_book(Books)
        search_book(Books)
    
    elif option=='3':
        clear_console()
        author=input(f"{" "*32}{cl['bold']}{cl['c_87']}Enter the author name:{cl['reset']} ")
        while not author:
            print(f"{" "*32}{cl['c_196']}Author can't be empty{cl['reset']}")
            author=input(f"{" "*32}{cl['bold']}Enter the author name:{cl['reset']}")
        not_found=True
        for index,book in enumerate(Books):
            for author_name in book['authors']:
                if author.lower()==author_name.lower():
                    display(book)
                    not_found=False
                    break
        
        if not_found:
            time.sleep(0.5)
            clear_console()
            print(f'\n\n{" "*32}{cl['bold']}{cl['c_196']}{" "*30}Sorry🥹 , No book has found for this author{cl['reset']}')
            #search_book(Books)
        search_book(Books)
    elif option=='4':
        clear_console()
        return 
    else:
        clear_console()
        print(f"{" "*30}🚫 🚫 🚫   {cl['c_196']}{cl['bold']}you have enter wrong input.   🚫 🚫 🚫\n")
        print(f"{" "*30}Please press 1️⃣  or 2️⃣  or 3️⃣  or 4️⃣ {cl['reset']}")
        search_book(Books)