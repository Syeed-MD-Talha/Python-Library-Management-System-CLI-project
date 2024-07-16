import time
from files.colors import clear_console,cl


def display_book(Books):
    clear_console()
    if not Books:
        print(f"{" "*50}{cl['c_200']}{cl['bold']}Book list is empty!!💤💤💤💤{cl['reset']}")
        time.sleep(1)
    for index, book in enumerate(Books):
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

        details=[
        f'{" "*32}{bold}{bright_magenta}{"="*30} 📖 {bold}{blue}Book no.{index+1} {magenta}{"="*30}{reset}',
        f'{" "*32}📝 {bold}Title:{reset}           {Italic}{bold}{yellow}"{book["title"]}"{reset}',
        f'{" "*32}✍️  {bold}Authors:{reset}         {blue}{", ".join(book["authors"])}{reset}',
        f'{" "*32}📕 {bold}ISBN:{reset}            {magenta}{book["isbn"]}{reset}',
        f'{" "*32}📅 {bold}Publishing Year:{reset} {red}{book["year"]}{reset}',
        f'{" "*32}💰 {bold}Price:{reset}           {cyan}${book["price"]:.2f}{reset}',
        f'{" "*32}🔢 {bold}Quantity:{reset}        {book["quantity"]}{reset}',
        f'{" "*32}{bold}{magenta}{"="*75}{reset}\n',
        ]

        for string in details:
            for ch in string:
                print(ch,end='')
                time.sleep(0.0009)
            print()
            time.sleep(0.01)
