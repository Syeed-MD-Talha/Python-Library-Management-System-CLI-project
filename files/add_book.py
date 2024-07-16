from files.colors import cl
from files.file_operations import update_info
import time
import re

def add_new_book(Books):
    title=input(f"{" "*32}{cl['bold']}{cl['c_195']}Enter the title{cl['reset']}(example:Harry potter) {cl['bold']}{cl['c_195']}of the book:{cl['reset']} ")
    if not title:
          print(f"{" "*32}{cl['c_196']}Title can't be empty{cl['reset']}")
          add_new_book(Books)
    

    authors_name=input(f'{" "*32}{cl['bold']}{cl['c_195']}Enter the authors name{cl['reset']}(example:talha,sayed) {cl['bold']}{cl['c_195']}of the book:{cl['reset']} ')
    authors=list(authors_name.split(','))
    pattern = r'^[A-Za-z, ]+$'
    valid=True
    for author in authors:
          valid&=bool(re.match(pattern, author))
    while not authors_name or not valid:
          if authors_name and not valid:print(f"{" "*32}{cl['c_196']}Authors name isn't valid{cl['reset']}")
          else:print(f"{" "*32}{cl['c_196']}Authors can't be empty{cl['reset']}")
          authors_name=input(f'{" "*32}{cl['bold']}{cl['c_195']}Enter the authors name:{cl['reset']}')
          authors=list(authors_name.split(','))
          valid=True
          for author in authors:
            valid&=bool(re.match(pattern, author))
          



    isbn=input(f"{" "*32}{cl['bold']}{cl['c_195']}Enter ISBN{cl['reset']}(example:11-23-34-33)  {cl['bold']}{cl['c_195']}of this book:{cl['reset']} ")
    valid_isbn=any(c in isbn for c in '0123456789')
    while not isbn or not valid_isbn:
        if not isbn:print(f"{" "*32}{cl['c_196']}ISBN can't be empty{cl['reset']}")
        else:print(f"{" "*32}{cl['c_196']}ISBN code is not valid{cl['reset']}")
        isbn=input(f"{" "*32}{cl['bold']}{cl['c_195']}Enter ISBN:{cl['reset']}")
        valid_isbn=any(d in isbn for d in '0123456789')


    publish_year=input(f"{" "*32}{cl['bold']}{cl['c_195']}Enter the published year{cl['reset']}(example:20/02/2024)  {cl['bold']}{cl['c_195']}of this book:{cl['reset']} ")
    valid_year = all(c in '/0123456789.-' for c in publish_year)
    while not publish_year or not valid_year:
        if not publish_year:print(f"{cl['c_196']}published year can't be empty{cl['reset']}")
        else:print(f"{" "*32}{cl['c_196']}published year is not valid{cl['reset']}")
        publish_year=input(f"{" "*32}{cl['bold']}Enter the published year:{cl['reset']}")
        valid_year = all(c in '/0123456789.-' for c in publish_year)
    
      
    while True:
          price=input(f"{" "*32}{cl['bold']}{cl['c_195']}Enter price{cl['reset']}(example:200.32)  {cl['bold']}{cl['c_195']}of this book:{cl['reset']} ")
          if not price:
                print(f"{" "*32}{cl['c_196']}price can't be empty{cl['reset']}")
                continue
          try:
               price=float(price)
               if price<=0:
                    print(f"{" "*32}{cl['c_196']}price should be positive{cl['reset']}")
                    continue
               break
          except ValueError:
               print(f"{" "*32}{cl['c_196']}Invalid input, please Enter valid price{cl['reset']}")



    while True:
          quantity=input(f"{" "*32}{cl['bold']}{cl['c_195']}Enter the quantity{cl['reset']}(example:50)  {cl['bold']}{cl['c_195']}of this book:{cl['reset']} ")
          if not quantity:
                print(f"{" "*32}{cl['c_196']}quantity can't be empty{cl['reset']}")
                continue
          try:
            quantity=int(quantity)
            if quantity<=0:
                  print(f"{" "*32}{cl['c_196']}quantity should be greater then 0{cl['reset']}")
                  continue
            break
          except ValueError:
               print(f"{" "*32}{cl['c_196']}Invalid input, please Enter valid price{cl['reset']}")
               
          

#     quantity=int(input("Enter the quantity of this book:"))
    Books.append(
          {
            'title':title,
            'authors':authors,
            'isbn':isbn,
            'year':publish_year,
            'price':price,
            'is_lent':False,
            'quantity':int(quantity),
            'book_Borrowers':[]
          }
    )
    time.sleep(0.7)
    print(f"{" "*32}{cl['bold']}{cl['c_10']}Book has been add successfully!!!!{cl['reset']}✅✅✅")
    update_info(Books)