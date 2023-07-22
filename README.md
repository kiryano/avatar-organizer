# Introduction
This was created out of boredom to automate the organization of avatar files and organize them properly, since I have issues doing that.... [changelog](https://github.com/kiryano/avatar-organizer/blob/main/changelog.md)🐈

## TODOs
- Implement Interactive Mode
- Logging Improvements
- Implement more safety measures
- Duplicate Detection Improvements
- Undo Functionality
- Configuration File

## Features

- Recursive search: The script searches for avatars in the current directory and subdirectories, ensuring all avatars are organized.
- Image verification: Each image is verified using OpenCV to ensure it is a valid image file.
- Fast preliminary duplicate detection: The script calculates the hash value for each image file and compares it with the encountered file hashes. Potential duplicate images with the same file hash are removed.
- Detailed duplicate comparison: For potential duplicates (those with unique file hashes), the script performs a more detailed comparison using OpenCV's `cv2.subtract()` function to confirm if they are true duplicates based on image content.
- Backup creation: A backup of each photo file is created in the `backup` directory to ensure data preservation.
- Random filename generation: Each photo file is moved to the target folder with a random filename to ensure uniqueness.
- Logging: The script logs the operations and outputs the results for easy tracking and debugging.

## Arguments

- `-t`, `--target`: Specify the target folder name (default: avatars).
- `-c`, `--confirm`: Prompt for confirmation before moving files.

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
  - **os**: Provides a way to interact with the operating system, such as creating directories and moving files.
  - **shutil**: Offers high-level file operations, such as copying and moving files.
  - **random**: Enables generating random names for files.
  - **string**: Provides a set of useful string constants and operations.
  - **cv2 (OpenCV)**: Allows image processing tasks, such as reading and comparing images.
  - **colorama**: Enables colored output in the console.
  - **logging**: Facilitates logging messages to a file.
  - **pyfiglet**: Allows generating ASCII art text.
  - **argparse**: Provides command-line argument parsing functionality.
  - **hashlib**: Offers hashing algorithms for generating file hashes.

## Feedback and Contributions
If you have any suggestions, feedback, or improvements for this script, feel free to submit a pull request on the GitHub repository.

## License
This script is released under the [MIT License](LICENSE).
