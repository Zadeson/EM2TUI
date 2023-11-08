import curses
from curses import panel
import os
import subprocess

# Configurable constants
EMULATOR_DIR = 'emulators'
EMULATOR_EXTENSIONS = ['.exe', '.bat', '.sh']  # Add more if needed
ROM_EXTENSIONS = ['.nes', '.snes', '.gb', '.gbc', '.gba', '.md', '.z64']  # Add more if needed
non_emulators = ['7za.exe'] # Add more if needed

# Function to scan for emulators and ROMs
def scan_for_emulators_and_roms(directory):
    emulators = []
    roms = {}
    # Scan for emulators in the 'emulators' directory
    emulator_dir_path = os.path.join(directory, EMULATOR_DIR)
    if os.path.exists(emulator_dir_path):
        for root, dirs, files in os.walk(emulator_dir_path):
            for file in files:
                if file not in non_emulators:  # Check if the file is not in the non_emulators list
                    name, ext = os.path.splitext(file)
                    if ext in EMULATOR_EXTENSIONS:
                        emulators.append(os.path.join(root, file))

    # Scan for ROMs anywhere in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            name, ext = os.path.splitext(file)
            if ext in ROM_EXTENSIONS:
                for emulator in emulators:
                    roms.setdefault(emulator, []).append(os.path.join(root, file))

    return roms

# Function to run the selected emulator with the selected ROM
def run_emulator(emulator, rom):
    subprocess.Popen([emulator, rom], close_fds=True)

# Function to draw tabs on a window
def draw_tabs(win, width, tab_titles, selected_idx):
    tab_width = width // len(tab_titles)-1
    for idx, title in enumerate(tab_titles):
        tab_start_x = idx * tab_width
        if idx == selected_idx:
            win.attron(curses.color_pair(1))
            win.addstr(1,  tab_start_x+1, title.center(tab_width))
            win.attroff(curses.color_pair(1))
        else:
            win.attron(curses.color_pair(2))
            win.addstr(1,  tab_start_x+1, title.center(tab_width))
            win.attroff(curses.color_pair(2))

# Function to draw list items centered horizontally
def draw_list(win, start_y, items, selected_idx, width, highlight_color, left_pad):
    for idx, item in enumerate(items):
        item_str = f'* {item}' if idx == selected_idx else f'  {item}'
        if idx == selected_idx:
            win.attron(highlight_color)
            win.addstr(start_y + idx, left_pad, item_str)
            win.attroff(highlight_color)
        else:
            win.addstr(start_y + idx, left_pad, item_str, curses.color_pair(1))

# Function to draw centered text in a window
def draw_centered_text(win, start_y, text, width, attribute=curses.A_NORMAL):
    for idx, line in enumerate(text.split('\n')):
        win.addstr(start_y + idx, max(0, (width - len(line)) // 2)+1, line, attribute)

# Curses TUI for selecting emulator and ROM
def menu(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal text
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlighted tab
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Highlighted list item

    roms_dict = scan_for_emulators_and_roms('.')
    emulators = list(roms_dict.keys())
    tabs = ['EMULATOR', 'ROM', 'QUIT']
    tab_idx = 0
    emulator_idx = 0
    rom_idx = 0

    # Fixed window dimensions
    width = 55  # 40 characters wide + 2 for borders
    height = 16  # 20 lines tall + 2 for borders

    # Create window centered in screen
    start_x = (curses.COLS - width) // 2
    start_y = (curses.LINES - height) // 2
    win = curses.newwin(height, width, start_y, start_x)
    win.keypad(True)  # Enable keypad mode

    # Function to display the menu
    def display_menu(tab_idx, emulator_idx, rom_idx):
        win.clear()
        win.box()

        # Draw the title in the top left of the border
        win.addstr(0, 2, ' EM2 TUI ', curses.color_pair(1) | curses.A_BOLD)

        # Draw tabs
        draw_tabs(win, width, tabs, tab_idx)

        # Determine the longest list length for centering
        list_width = max(len(os.path.basename(emu)) for emu in emulators) + 4  # 4 for "* " and "  "
        left_pad = (width - list_width) // 2  # Center the list column

        # Draw list items based on selected tab
        if tab_idx == 0:  # Emulator tab
            win.addstr(3, 3, "THIS IS THE BETA VERSION OF EM2 <TUI>")
            win.addstr(4, 3, "WRITTEN IN PY CURSES WIN64 2023")
            win.addstr(6, 3, "EMULATORS:")
            draw_list(win, 8, [os.path.basename(emu) for emu in emulators], emulator_idx, width, curses.color_pair(3), left_pad)
        elif tab_idx == 1:  # ROM tab
            if emulators:
                win.addstr(3, 3, "THIS IS THE BETA VERSION OF EM2 <TUI>")
                win.addstr(4, 3, "WRITTEN IN PY CURSES WIN64 2023")
                win.addstr(6, 3, "ROMS:")
                draw_list(win, 8, [os.path.basename(rom) for rom in roms_dict[emulators[emulator_idx]]], rom_idx, width, curses.color_pair(3), left_pad)

        # Draw instructions
        win.addstr(height - 2, 2, "Navigate with arrow keys, Enter to select", curses.color_pair(1))

        win.refresh()

    # Resize terminal to fit the window
    os.system(f'resize -s {height} {width}')

    # Main loop
    while True:
        display_menu(tab_idx, emulator_idx, rom_idx)
        key = win.getch()

        if key == curses.KEY_LEFT and tab_idx > 0:
            tab_idx -= 1
            rom_idx = 0  # Reset ROM index when switching tabs
        elif key == curses.KEY_RIGHT and tab_idx < len(tabs) - 1:
            tab_idx += 1
            rom_idx = 0  # Reset ROM index when switching tabs
        elif key == curses.KEY_UP and tab_idx == 0 and emulator_idx > 0:
            emulator_idx -= 1
        elif key == curses.KEY_DOWN and tab_idx == 0 and emulator_idx < len(emulators) - 1:
            emulator_idx += 1
        elif key == curses.KEY_UP and tab_idx == 1 and rom_idx > 0:
            rom_idx -= 1
        elif key == curses.KEY_DOWN and tab_idx == 1 and rom_idx < len(roms_dict[emulators[emulator_idx]]) - 1:
            rom_idx += 1
        elif key == ord('\n') and tab_idx == 1:  # Launch emulator with ROM
            run_emulator(emulators[emulator_idx], roms_dict[emulators[emulator_idx]][rom_idx])
            win.addstr(height - 2, 2, "Launching emulator... Press any key to exit.", curses.A_BOLD)
            win.refresh()
            win.getch()
            break
        elif key == ord('q') or key == ord('Q') or (key == ord('\n') and tab_idx == 2):
            break


# Run the TUI
def main():
    curses.wrapper(menu)

if __name__ == "__main__":
    main()
