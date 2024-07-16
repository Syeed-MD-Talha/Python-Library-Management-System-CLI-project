import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



# Create dictionaries for all 256 foreground and background colors
cl = {f'c_{i}': f'\033[38;5;{i}m' for i in range(256)}
bg_colors = {f'bg_color_{i}': f'\033[48;5;{i}m' for i in range(256)}

# Reset code
reset = "\033[0m"
cl['Italic']= "\033[3m"
cl['reset'] = "\033[0m"
cl['bold'] = "\033[1m"
cl['underline'] = "\033[4m"

# # Example usage: print all 256 foreground colors
# for name, code in fg_colors.items():
#     print(f"{code}{name}{reset}", end=" ")
#     # if (int(name.split('_')[-1]) + 1) % 16 == 0:
#     #     print()  # New line every 16 colors

# # Example usage: print all 256 background colors
# print()  # Separate the two examples with a new line
# for name, code in bg_colors.items():
#     print(f"{code}{name}{reset}", end=" ")
#     if (int(name.split('_')[-1]) + 1) % 16 == 0:
#         print()  # New line every 16 colors
