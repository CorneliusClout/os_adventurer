from utils import print_with_backspace, simulate_typing

def load_area_texts(file_path):
    area_texts = {}
    current_area = None

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            line = line.strip()
            if line.endswith(';'):
                current_area = line[:-1].strip()
                area_texts[current_area] = []
            else:
                if current_area:
                    if not line:  # If it's an empty line, consider it as a separate item
                        area_texts[current_area].append("EMPTY_LINE_TOKEN")
                        continue
                    else:
                        area_texts[current_area].append(line)
    return area_texts

# Function to get text for a specific area
def text_printer(area_texts, room_name, current_room):

    current_text = area_texts.get(room_name)
    if current_text is not None:
        for item in current_text:
            if item == "EMPTY_LINE_TOKEN":
                print("\n")

            else:
                simulate_typing(item)  # Print only if normal_text flag is set

def acsii_printer(room):
    """
    Print de ASCII-art voor de opgegeven kamer.
    """
    if room.acsii_art:
        print(f"ASCII-art voor {room.room_name}:")
        for line in room.acsii_art:
            print(line)
    else:
        print(f"Geen ASCII-art gevonden voor {room.room_name}.")