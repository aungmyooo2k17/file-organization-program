# File Organization Program

This Python program organizes files in a specified directory based on their file types. It categorizes files into folders such as Audio, Documents, Images, etc., according to predefined file type associations.

## Features

- Organizes files into folders based on their types.
- Handles various file types such as Audio, Documents, Images, etc.
- Easy customization of file type associations.

## How to Use

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/file-organization-program.git
    cd file-organization-program
    ```

2. **Run the Program:**

    ```bash
    python main.py
    ```

    You will be prompted to enter the path to the directory you want to organize.

3. **Customization:**

    Edit the `folder_names` dictionary in `main.py` to customize the file type associations.

    ```python
    folder_names = {
        "Audio": {"aif", "cda", "mid", "midi", "mp3", "mpa", "ogg", "wav", "wma"},
        "Compressed": {"7z", "deb", "pkg", "rar", "rpm", "tar.gz", "z", "zip"},
        # ... (other file types)
    }
    ```

## Example

Suppose you have the following directory structure: