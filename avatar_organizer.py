import os
import shutil
import random
import string
import cv2
from colorama import Fore
import logging
import pyfiglet
import argparse
import hashlib

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
    confirmation = input(Fore.GREEN + 'Do you want to proceed with organizing the avatars? (y/n): ')
    if confirmation.lower() != 'y':
        print(Fore.RED + 'Operation cancelled.')
        exit()

backup_dir = 'backup'
if not os.path.exists(backup_dir):
    try:
        os.mkdir(backup_dir)
    except OSError as e:
        logging.error(f'Error creating the backup directory: {str(e)}')
        print(Fore.RED + f'Error creating the backup directory: {str(e)}')

file_extensions = ['jpg', 'jpeg', 'png', 'gif']


# Recursive function to search for avatars in subdirectories
def search_avatars(directory):
    avatars = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(tuple(file_extensions)):
                avatars.append(os.path.join(root, file))
    return avatars


def calculate_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


def verify_image(file_path):
    try:
        image = cv2.imread(file_path)
        if image is None:
            return False
        return True
    except cv2.error as error:
        logging.warning(f'Error reading image file: {file_path} ({str(error)})')
        print(Fore.RED + f'Warning: Error reading image file: {file_path} ({str(error)})')
        return False
    except Exception as error:
        logging.warning(f'Error processing image file: {file_path} ({str(error)})')
        print(Fore.RED + f'Warning: Error processing image file: {file_path} ({str(error)})')
        return False


# Find all avatars in the current directory and subdirectories
avatars = search_avatars('.')

if len(avatars) == 0:
    logging.error('No files found with the specified extensions.')
    print(Fore.RED + 'Error: No files found with the specified extensions.')
    exit()

encountered_images = []
for file in avatars:
    try:
        if not verify_image(file):
            logging.warning(f'Invalid file: {file}')
            print(Fore.RED + f'Warning: Invalid file: {file}')
            continue

        # Calculate file hash for fast preliminary duplicate detection
        file_hash = calculate_file_hash(file)

        # Check for potential duplicates based on file hash
        if file_hash in encountered_images:
            logging.warning(f'Duplicate image found: {file}')
            print(Fore.RED + f'Warning: Duplicate image found: {file}')
            os.remove(file)  # Delete the duplicate file
            continue

        encountered_images.append(file_hash)

        # Create a backup of the files in the backup directory
        try:
            shutil.copy2(file, os.path.join(backup_dir, os.path.basename(file)))
            logging.info(f'Created backup: {file} -> {backup_dir}/{os.path.basename(file)}')
        except OSError as e:
            logging.error(f'Error creating the backup file: {file} ({str(e)})')
            print(Fore.RED + f'Error creating the backup file: {file} ({str(e)})')

        # Move the files to the target folder with a random filename
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        new_filename = f'{random_name}.{file.rsplit(".", 1)[1]}'
        try:
            shutil.move(file, os.path.join(target_folder, new_filename))
            logging.info(f'Moved file: {file} -> {target_folder}/{new_filename}')
        except OSError as e:
            logging.error(f'Error moving the file: {file} ({str(e)})')
            print(Fore.RED + f'Error moving the file: {file} ({str(e)})')

    except (IOError, SyntaxError, TypeError) as e:
        logging.warning(f'Invalid file: {file} ({str(e)})')
        print(Fore.RED + f'Warning: Invalid file: {file} ({str(e)})')


print(Fore.BLUE + 'Your avatars have been organized and moved to the target folder with random filenames.')
