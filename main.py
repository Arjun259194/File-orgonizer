import os
import shutil
import easygui


def create_directories(dir):
    directories_needed = {
        os.path.join(dir, "images"),
        os.path.join(dir, "docs"),
        os.path.join(dir, "videos"),
        os.path.join(dir, "executables"),
        os.path.join(dir, "zips"),
        os.path.join(dir, "audios"),
        os.path.join(dir, "others"),
    }

    for path in directories_needed:
        if not os.path.isdir(path):
            os.mkdir(path)


def move_file(file_extension, file_path, directory):
    if(file_extension == "png" or file_extension == "jpg" or file_extension == "jpeg" or file_extension == "webp"):
        shutil.move(file_path, os.path.join(directory, "images"))
    elif(file_extension == "exe"):
        shutil.move(file_path, os.path.join(directory, "executables"))
    elif(file_extension == "mp4"):
        shutil.move(file_path, os.path.join(directory, "videos"))
    elif(file_extension == "txt" or file_extension == "doc" or file_extension == "docx" or file_extension == "pdf"):
        shutil.move(file_path, os.path.join(directory, "docs"))
    elif(file_extension == "zip"):
        shutil.move(file_path, os.path.join(directory, "zips"))
    elif(file_extension == "mp3"):
        shutil.move(file_path, os.path.join(directory, "audios"))
    else:
        shutil.move(file_path, os.path.join(directory, "others"))


def main():
    directory = easygui.diropenbox()

    if not directory:
        print("directory not selected")

    if not os.path.isdir(directory):
        return print("entered path is not a valid path in your system")

    create_directories(directory)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_extension = filename.split('.')[-1]

        if not os.path.isfile(file_path):
            continue

        move_file(file_extension, file_path, directory)


if __name__ == "__main__":
    main()
