import os

terminal_size = os.get_terminal_size().columns
print(f"The number of characters per line is: {terminal_size}")