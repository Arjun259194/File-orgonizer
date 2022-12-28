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

    image_file_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    executable_file_extensions = ['.exe', '.msi', '.bat', '.cmd', '.vbs']
    zip_file_extensions = ['.zip', '.7z', '.tar', '.gz']
    text_file_extensions = ['.txt', '.rtf', '.doc',
                            '.docx', '.odt', '.pdf', '.ppt', '.pptx']
    video_file_extensions = ['.avi', '.mp4', '.mov',
                             '.wmv', '.mkv', '.flv', '.mpg', '.mpeg']
    audio_file_extensions = ['.mp3', '.wav',
                             '.wma', '.aac', '.flac', '.m4a', '.amr']

    if(file_extension in image_file_extensions):
        shutil.move(file_path, os.path.join(directory, "images"))
    elif(file_extension in executable_file_extensions):
        shutil.move(file_path, os.path.join(directory, "executables"))
    elif(file_extension in video_file_extensions):
        shutil.move(file_path, os.path.join(directory, "videos"))
    elif(file_extension in text_file_extensions):
        shutil.move(file_path, os.path.join(directory, "docs"))
    elif(file_extension in zip_file_extensions):
        shutil.move(file_path, os.path.join(directory, "zips"))
    elif(file_extension in audio_file_extensions):
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
        file_extension = os.path.splitext(filename)[1]
        if not os.path.isfile(file_path):
            continue
        move_file(file_extension, file_path, directory)


if __name__ == "__main__":
    main()
