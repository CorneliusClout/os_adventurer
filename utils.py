import time
import sys
from room import Room
from edible import Edible
from event import Event
import shutil  # Import shutil for terminal width detection

def simulate_typing(text):
    terminal_width = shutil.get_terminal_size().columns

    chars_per_line = 0

    for char in text:
        print(char, end='', flush=True)
        chars_per_line += 1

        if chars_per_line >= terminal_width:
            print()  # Wrap to the next line
            chars_per_line = 0

        time.sleep(0.01)
    
    print()  # Add a newline after typing all characters
    return ''

def print_with_backspace(text):
    terminal_width = shutil.get_terminal_size().columns
    chars_per_line = 0
    lines_printed = 0

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        chars_per_line += 1

        if chars_per_line >= terminal_width:
            lines_printed += 1
            chars_per_line = 0

        time.sleep(0.01)

    time.sleep(5)  # Delay to show the effect before backspacing

    for _ in range(len(text) + lines_printed):
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        chars_per_line -= 1

        if chars_per_line < 0:
            chars_per_line = terminal_width - 1  # Wrap to the previous line

        time.sleep(0.01)

    print()  # Add a newline after backspacing
    time.sleep(5)  # Delay to show the effect before backspacing
    
    for _ in range(len(text)):
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        chars_per_line -= 1

        if chars_per_line < 0:
            chars_per_line = terminal_width - 1  # Wrap to the previous line

        time.sleep(0.01)

    print()  # Add a newline after backspacing
def generate_health_bar(energie, moshiness, humeur):
    #generate energie
    num_blocks_energie = energie // 5  # Calculate the number of '#' blocks
    num_empty_blocks_energie = 20 - num_blocks_energie  # Calculate the number of '-' blocks

    health_bar = '[' + '#' * num_blocks_energie + '-' * num_empty_blocks_energie + ']'
    
    #generate moshiness
    num_blocks_moshiness = moshiness // 5  # Calculate the number of '#' blocks
    num_empty_blocks_moshiness = 20 - num_blocks_moshiness  # Calculate the number of '-' blocks

    mosh_bar = '[' + '@' * num_blocks_moshiness + '-' * num_empty_blocks_moshiness + ']'
    
    #generate humeur
    num_blocks_humeur = humeur // 5  # Calculate the number of '#' blocks
    num_empty_blocks_humeur = 20 - num_blocks_humeur  # Calculate the number of '-' blocks

    humeur_bar = '[' + '%' * num_blocks_humeur + '-' * num_empty_blocks_humeur + ']'
    
    #PRINT ZE
    simulate_typing("ENERGIE:\n")
    simulate_typing(health_bar)
    simulate_typing(str(energie))
    simulate_typing("MOSHINESS:\n")
    simulate_typing(mosh_bar)
    simulate_typing(str(moshiness))
    simulate_typing("HUMEUR:\n")
    simulate_typing(humeur_bar)
    simulate_typing(str(humeur))
    return ''