# Avatar Organizer

## Introduction
This was created out of boredom to automate the organization of avatar files and organize them properly, since I have issues doing that.... 🐈

## Features
- Moves avatar files containing the extensions of (e.g., JPG, JPEG, PNG, GIF) into a folder named "avatars"
- Generates a random string for the filenames
- Error handling for cases such as existing "avatars" folder and no avatar files found
- Very easy to setup and use
- Checks to verify the validity of the avatar files before moving them
- Automatic backup or copy of each file in a separate directory before moving them
- Better organization by (e.g., sorting by date, size, etc.)
- Recursive method to search for avatar files in subdirectories
- Very interactive & user friendly by having user prompts & command-line arguments.

## TODOs
- [x] Implement a check to verify the validity of the avatar files before moving them
- [x] Implement creating a backup or copy of each file in a separate directory before moving them.
- [x] Implement a better way to organize files (e.g., sorting by date, size, etc.).
- [x] Implement a recursive method to search for avatar files in subdirectories.
- [x] Make the script more interactive, with user prompts or command-line arguments.
- [x] Enhance Error Handling
- [x] Implement a check to identify and handle duplicate files.
- [ ] Implement where users can specify specific files or directories to exclude from the organizing process
- [ ] Add more user interaction?
- [ ] Implement additional sorting options
- [ ] Enhance the backup functionality
- [ ] Add checks to see if the required modules are installed, if not, install them

## Usage
1. Clone the repository or head over to the [releases](https://github.com/kiryano/avatar-organizer/releases/tag/v1.0.0): `git clone https://github.com/kiryano/avatar-organizer.git`
2. Place the script file in the directory containing the avatar files you want to organize.
3. Open up a terminal and navigate to the directory where the script is located.
4. Run the script using the following command: `python avatar_organizer.py`
5. The script will create a folder named "avatars" (if it doesn't already exist lol) and move the photo files into it with a random generated string for the filenames.
6. Check the "avatars" folder to find your avatar files.

## Customization
- Supported file extensions: By default, the script supports the following extensions: JPG, JPEG, PNG, and GIF. You can customize the list of supported extensions by modifying the `avatar_extensions` variable in the script.
- Filename length: The random filenames generated are 10 characters long. If you want to change the length, you can modify the `k` parameter in the `random.choices` function in the script.


## Requirements
- Python 3.x
- Required Python Modules:
  - os
  - shutil
  - random
  - string
  - colorama
  - logging
  - pillow
  - pyfiglet
  - hashlib

## Disclaimer
This script was created for educational and recreational purposes. Please use it responsibly and ensure that you have appropriate permissions to modify and organize the files in your directory, also make sure to backup any files beforehand :3

## Feedback and Contributions
If you have any suggestions, feedback, or improvements for this script, feel free to submit a pull request on the GitHub repository.

## License
This script is released under the [MIT License](LICENSE).
