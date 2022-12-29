import os


def image_file_extensions():
    return ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']


def executable_file_extensions():
    return ['.exe', '.msi', '.bat', '.cmd', '.vbs']


def zip_file_extensions():
    return ['.zip', '.7z', '.tar', '.gz']


def text_file_extensions():
    return ['.txt', '.rtf', '.doc', '.docx', '.odt', '.pdf', '.ppt', '.pptx']


def video_file_extensions():
    return ['.avi', '.mp4', '.mov', '.wmv', '.mkv', '.flv', '.mpg', '.mpeg']


def audio_file_extensions():
    return ['.mp3', '.wav', '.wma', '.aac', '.flac', '.m4a', '.amr']


def get_directory_list(dir):
    return {
        os.path.join(dir, "Images"),
        os.path.join(dir, "Docs"),
        os.path.join(dir, "Videos"),
        os.path.join(dir, "Executables"),
        os.path.join(dir, "Zips"),
        os.path.join(dir, "Audios"),
        os.path.join(dir, "Others"),
    }
