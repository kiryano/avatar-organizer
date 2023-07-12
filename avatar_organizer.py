import os
import shutil
import random
import string
from PIL import Image
from colorama import Fore, Style
import logging
import pyfiglet
import argparse

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='avatar_organizer.log'
)

ascii_text = pyfiglet.figlet_format("avatar organizer by marc", font="slant", width=150)
description = 'A script to organize your avatars into a target folder with random filenames.'
usage = 'Usage: python avtar_organizer.py [-h] [-t TARGET] [-c]'
print(Fore.BLUE + ascii_text)
print(Fore.LIGHTBLUE_EX + description)
print(Fore.LIGHTBLUE_EX + usage)

parser = argparse.ArgumentParser(description='Avatar Organizer')
parser.add_argument('-t', '--target', default='avatars', help='Specify the target folder name (default: avatars)')
parser.add_argument('-c', '--confirm', action='store_true', help='Prompt for confirmation before moving files')
args = parser.parse_args()

# Check if the target folder already exists
target_folder = args.target
if not os.path.exists(target_folder):
    try:
        os.mkdir(target_folder)
    except OSError as e:
        logging.error(f'Error creating the "{target_folder}" folder: {str(e)}')
        print(Fore.RED + f'Error creating the "{target_folder}" folder: {str(e)}')
        exit()
else:
    logging.warning(f'The "{target_folder}" folder already exists.')

if args.confirm:
    confirmation = input(Fore.GREEN + 'Do you want to proceed with organizing the photo files? (y/n): ')
    if confirmation.lower() != 'y':
        print(Fore.RED + 'Operation cancelled.')
        exit()

# Create the backup directory if it doesn't exist
backup_dir = 'backup'
if not os.path.exists(backup_dir):
    try:
        os.mkdir(backup_dir)
    except OSError as e:
        logging.error(f'Error creating the backup directory: {str(e)}')
        print(Fore.RED + f'Error creating the backup directory: {str(e)}')

photo_extensions = ['jpg', 'jpeg', 'png', 'gif']


# Recursive function to search for photo files in subdirectories
def search_avatars(directory):
    avatars = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(tuple(photo_extensions)):
                avatars.append(os.path.join(root, file))
    return avatars


# Find all photo files in the current directory and subdirectories
avatars = search_avatars('.')

# Check if any photo files were found
if len(avatars) == 0:
    logging.error('No avatars were found with the specified extensions.')
    print(Fore.RED + 'Error: No avatars found with the specified extensions.')
    exit()

# Sort the photo files based on modification date in ascending order
sorted_files = sorted(avatars, key=os.path.getmtime)

# Move each valid photo file to the target folder with a random filename
for file in sorted_files:
    try:
        # This will validate the image
        with Image.open(file) as img:
            img.verify()

        # Create a backup of the file in the backup directory
        try:
            shutil.copy(file, os.path.join(backup_dir, os.path.basename(file)))
            logging.info(f'Created backup: {file} -> {backup_dir}/{os.path.basename(file)}')
        except OSError as e:
            logging.error(f'Error creating the backup file: {file} ({str(e)})')
            print(Fore.RED + f'Error creating the backup file: {file} ({str(e)})')

        # Move the file to the target folder with a random filename
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        new_filename = f'{random_name}.{file.rsplit(".", 1)[1]}'
        try:
            shutil.move(file, os.path.join(target_folder, new_filename))
            logging.info(f'Moved file: {file} -> {target_folder}/{new_filename}')
        except OSError as e:
            logging.error(f'Error moving the file: {file} ({str(e)})')
            print(Fore.RED + f'Error moving the file: {file} ({str(e)})')
    except (IOError, SyntaxError) as e:
        logging.warning(f'Invalid photo file: {file} ({str(e)})')
        print(Fore.YELLOW + f'Warning: Invalid photo file: {file} ({str(e)})')

print(Fore.BLUE + 'Your avatars have been organized and moved to the target folder with random filenames.')
