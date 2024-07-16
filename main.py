
from files.display import display_book
from files.add_book import add_new_book
from files.searchBook import search_book
from files.removeBook import remove_book
from files.lend_Book import book_lending_system
from files.file_operations import fetchData_from_file
from files.colors import cl
from files.colors import clear_console
import time


Books =[]
Books=fetchData_from_file()


clear_console()
while(True):
    
    print(f'\n\n {" "*30}',end='')
    st='⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛      Welcome to Library Management System     ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛'
    st1=' ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛'
    for ch in st:
            if ch=='⚛':print(f'{cl["c_87"]}{ch}{cl["reset"]}',end='')
            else:print(f'{cl["c_81"]}{cl["bold"]}{ch}{cl["reset"]}',end='')
            time.sleep(0.02)
    print()
    print (f'{" "*30} {cl["c_87"]}⚛{cl["reset"]}                                                                           {cl["c_87"]}⚛{cl["reset"]}')
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                 {cl["c_192"]}{cl["bold"]}Press 1{cl["reset"]}   {cl["c_208"]}to display all information's{cl["reset"]}                    {cl["c_87"]}⚛{cl["reset"]}")
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                 {cl["bold"]}{cl["c_192"]}Press 2{cl["reset"]}   {cl["c_208"]}to add new  book{cl["reset"]}                                {cl["c_87"]}⚛{cl["reset"]}")
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                 {cl["bold"]}{cl["c_192"]}Press 3{cl["reset"]}   {cl["c_208"]}to search book{cl["reset"]}                                  {cl["c_87"]}⚛{cl["reset"]}")
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                 {cl["bold"]}{cl["c_192"]}Press 4{cl["reset"]}   {cl["c_208"]}to remove a book{cl["reset"]}                                {cl["c_87"]}⚛{cl["reset"]}")
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                 {cl["bold"]}{cl["c_192"]}Press 5{cl["reset"]}   {cl["c_208"]}to Lend book/return book/Lend_book details{cl["reset"]}      {cl["c_87"]}⚛{cl["reset"]}")
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                 {cl["bold"]}{cl["c_192"]}Press #{cl["reset"]}   {cl["c_85"]}to exit{cl["reset"]}                                         {cl["c_87"]}⚛{cl["reset"]}")
    print (f" {" "*30}{cl["c_87"]}⚛{cl["reset"]}                                                                           {cl["c_87"]}⚛{cl["reset"]}")
    print(f'{" "*30}',end='')
    for ch in st1:
        print(f'{cl["c_87"]}{ch}{cl["reset"]}',end='')
        time.sleep(0.02)
    # print(f' {" "*30}{cl["c_87"]}⚛{cl["reset"]} ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ ⚛ {cl["reset"]}')
    option=input(f'\n\n{" "*32}{cl["bold"]}choose option:{cl["reset"]}')
    if option=='1':display_book(Books)
    elif option=='2':add_new_book(Books)
    elif option=='3':search_book(Books)
    elif option=='4':remove_book(Books)
    elif option=='5':book_lending_system(Books)
    elif option=='#':break  
    else:
        clear_console()
        time.sleep(0.4)
        print(f'\n\n{" "*50}',end='')
        st='Please choose option between 1 to 5'
        for ch in st:
            print(f'{cl["c_196"]}{cl["bold"]}{ch}{cl["reset"]}',end='')
            time.sleep(0.07)


