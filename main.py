import os
import sys
from pathlib import Path

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

    [
        Path(eachfile).rename(
            new_path(eachfile, extension_filetype_map, path_to_organize)
        )
        for eachfile in onlyfiles
    ]

    # Move other folders
    [
        Path(onlyfolder).rename(
            os.path.join(path_to_organize, "Others", os.path.basename(onlyfolder))
        )
        for onlyfolder in onlyfolders
        if os.path.basename(onlyfolder) not in folder_names.keys()
    ]


def new_path(old_path, extension_filetype_map, path_to_organize):
    extension = str(old_path).split(".")[-1]
    amplified_folder = extension_filetype_map.get(extension, "Others")
    final_path = os.path.join(
        path_to_organize, amplified_folder, os.path.basename(old_path)
    )
    return final_path


# Extract list of files/folders


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        path = args[1]
        organize_files(path)
    else:
        print("Too many or no args are provided.")
