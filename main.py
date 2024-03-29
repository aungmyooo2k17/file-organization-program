import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

from click import File

# Get the file types

folder_names = {
    "Audio": {"aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma"},
    "Compressed": {"7z", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip"},
    "Code": {"js", "jsp", "html", "ipynb", "py", "java", "css"},
    "Documents": {
        "ppt",
        "pptx",
        "pdf",
        "xls",
        "xlsx",
        "doc",
        "docx",
        "txt",
        "tex",
        "epub",
    },
    "Images": {"bmp", "gif", "ico", "jpeg", "jpg", "png", "jfif", "svg", "tif", "tiff"},
    "Softwares": {"apk", "bat", "bin", "exe", "jar", "msi", "py"},
    "Videos": {"3gp", "avi", "flv", "h264", "mkv", "mov", "mp4", "mpg", "mpeg", "wmv"},
    "Others": {"NONE"},
}


def organize_files(path_to_organize):
    if not os.path.isdir(path_to_organize):
        print(f"Error: {path_to_organize} is not a valid directory.")
        sys.exit(1)

    onlyfiles = [
        os.path.join(path_to_organize, file)
        for file in os.listdir(path_to_organize)
        if os.path.isfile(os.path.join(path_to_organize, file))
    ]

    onlyfolders = [
        os.path.join(path_to_organize, file)
        for file in os.listdir(path_to_organize)
        if not os.path.isfile(os.path.join(path_to_organize, file))
    ]

    extension_filetype_map = {
        extension: fileType
        for fileType, extensions in folder_names.items()
        for extension in extensions
    }

    # make folders

    folder_paths = [
        os.path.join(path_to_organize, folder_name)
        for folder_name in folder_names.keys()
    ]

    [os.makedirs(folderPath, exist_ok=True) for folderPath in folder_paths]

    # Move desire folders
    for eachfile in onlyfiles:
        if(not Path(eachfile).exists()):
            Path(eachfile).rename(
                new_path(eachfile, extension_filetype_map, path_to_organize)
            )
        else:
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name, file_extension = Path(eachfile).stem, Path(eachfile).suffix
            shutil.move(Path(eachfile), new_path(f"{file_name}_{current_datetime}{file_extension}", extension_filetype_map, path_to_organize))
     
    # Move other folders
    for onlyfolder in onlyfolders:
        if os.path.basename(onlyfolder) not in folder_names.keys():
            if(not Path(onlyfolder).exists()):
                Path(onlyfolder).rename(os.path.join(path_to_organize, "Others", os.path.basename(onlyfolder)))
            else:
                current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
                shutil.move(Path(onlyfolder), new_path(f"{onlyfolder}_{current_datetime}", extension_filetype_map, path_to_organize))


def new_path(old_path, extension_filetype_map, path_to_organize):
    extension = str(old_path).split(".")[-1]
    amplified_folder = extension_filetype_map.get(extension, "Others")
    final_path = os.path.join(
        path_to_organize, amplified_folder, os.path.basename(old_path)
    )
    return final_path


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        path = args[1]
        organize_files(path)
    else:
        print("Too many or no args are provided.")
