import os
import shutil
import tempfile
import unittest

from main import organize_files


class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()

        # Create some test files and folders
        self.create_test_files()

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def create_test_files(self):
        # Create some test files in the temporary directory
        file_names = [
            "file1.mp3",
            "file2.pdf",
            "file3.py",
            "file4.txt",
            "file5.jpg",
            "file6.zip",
            "file7.unknown",
        ]
        for file_name in file_names:
            file_path = os.path.join(self.test_dir, file_name)
            open(file_path, "a").close()

        # Create some test folders in the temporary directory
        folder_names = ["Audio", "Documents", "Images", "Others"]
        for folder_name in folder_names:
            folder_path = os.path.join(self.test_dir, folder_name)
            os.makedirs(folder_path)

    def test_organize_files_with_invalid_arguments(self):
        with self.assertRaises(SystemExit) as cm:
            organize_files(f"{self.test_dir}/invalid_file.exe")
        self.assertEqual(cm.exception.code, 1)

    def test_organize_files(self):
        # Call the organize_files function with the test directory
        organize_files(self.test_dir)

        # Check if files are moved to the correct folders
        expected_folders = ["Audio", "Documents", "Images", "Others"]
        for folder_name in expected_folders:
            folder_path = os.path.join(self.test_dir, folder_name)
            self.assertTrue(os.path.exists(folder_path))
            files_in_folder = os.listdir(folder_path)
            self.assertTrue(files_in_folder)

        # Check if files are moved to the "Others" folder
        others_folder = os.path.join(self.test_dir, "Others")
        self.assertTrue(os.path.exists(others_folder))
        files_in_others = os.listdir(others_folder)
        self.assertEqual(files_in_others, ["file7.unknown"])

        # Check if files are moved to the "Images" folder
        others_folder = os.path.join(self.test_dir, "Images")
        self.assertTrue(os.path.exists(others_folder))
        files_in_others = os.listdir(others_folder)
        self.assertEqual(files_in_others, ["file5.jpg"])


if __name__ == "__main__":
    unittest.main()
