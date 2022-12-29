import os
import shutil
import easygui

from modules import *


def create_directories(dir):
    directories_needed = get_directory_list(dir)

    for path in directories_needed:
        if not os.path.isdir(path):
            os.mkdir(path)


def get_file_directory(file_extension):
    if(file_extension in image_file_extensions()):
        return "Images"
    elif(file_extension in executable_file_extensions()):
        return "Executables"
    elif(file_extension in video_file_extensions()):
        return "Videos"
    elif(file_extension in text_file_extensions()):
        return "Docs"
    elif(file_extension in zip_file_extensions()):
        return "Zips"
    elif(file_extension in audio_file_extensions()):
        return "Audios"
    else:
        return "Others"


def move_file(file_extension, file_path, directory):
    shutil.move(file_path, os.path.join(
        directory, get_file_directory(file_extension)))


def main():
    directory = easygui.diropenbox()
    if not directory:
        print("directory not selected")
    if not os.path.isdir(directory):
        return print("entered path is not a valid path in your system")
    create_directories(directory)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_extension = os.path.splitext(filename)[1]
        if not os.path.isfile(file_path):
            continue
        move_file(file_extension, file_path, directory)


if __name__ == "__main__":
    main()
