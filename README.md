# EM2 TUI

![EM2 TUI Screenshot](/tui.PNG)

EM2 TUI is a Terminal User Interface (TUI) for easily selecting and running emulators and ROMs from a simple curses-based interface. It's designed to work on Unix-like systems with Python and curses support, providing a quick and straightforward way to launch your favorite games using the associated emulators.

## Features

- Scans for emulators and ROMs within a specified directory.
- Supports a variety of emulator and ROM file extensions.
- Simple navigation using arrow keys with a clean, intuitive interface.
- Easy to extend and customize for additional emulators and ROM types.

## Prerequisites

Before you can run EM2 TUI, you need to make sure you have Python installed on your system and the necessary permissions to execute Python scripts. Additionally, your system needs to have `curses` support, which is typically available by default on most Unix-like systems.

## Installation

To install EM2 TUI, clone the repository or download the source code to your local machine:

```
git clone https://github.com/yourusername/em2-tui.git
cd em2-tui
```

## Usage

To start EM2 TUI, run the main script from the terminal:

```
python em2_tui.py
```

Navigate through the TUI using the arrow keys:
- Use the left and right arrows to switch between the EMULATOR, ROM, and QUIT tabs.
- Use the up and down arrows to scroll through the list of emulators or ROMs.
- Press Enter to launch the selected emulator with the selected ROM.
- Press 'q' or 'Q', or select the QUIT tab and press Enter to exit the application.

## Configuration

The `EMULATOR_DIR`, `EMULATOR_EXTENSIONS`, and `ROM_EXTENSIONS` constants can be configured to specify the directory of your emulators and the file extensions that your emulators and ROMs use. Add additional extensions as needed.

## Contributing

Contributions to EM2 TUI are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Hat tip to anyone whose code was used as inspiration.
- Special thanks to the community for any contributions.

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository or contact the maintainer at ethendixon@outlook.com.

Enjoy your retro gaming experience with EM2 TUI!
