import os
import shutil
from typing import List, Tuple

class FileProcessor:
    @staticmethod
    def copy_directory(source_dir: str, target_dir: str) -> None:
        """
        Copies all contents from source directory to target directory.
        Creates target directory if it doesn't exist.
        """
        try:
            # Create target directory if it doesn't exist
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            # Copy all contents including subdirectories
            for item in os.listdir(source_dir):
                source_path = os.path.join(source_dir, item)
                target_path = os.path.join(target_dir, item)
                
                if os.path.isdir(source_path):
                    shutil.copytree(source_path, target_path)
                else:
                    shutil.copy2(source_path, target_path)
        except Exception as e:
            raise Exception(f"Error copying directory: {str(e)}")

    @staticmethod
    def process_files(directory: str, extensions: List[str]) -> List[Tuple[str, int]]:
        """
        Processes files with specified extensions and returns list of tuples with filename and line count.
        """
        result = []
        try:
            for filename in os.listdir(directory):
                if any(filename.endswith(ext) for ext in extensions):
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path):
                        with open(file_path, 'r', encoding='utf-8') as file:
                            line_count = sum(1 for _ in file)
                            result.append((filename, line_count))
            return result
        except Exception as e:
            raise Exception(f"Error processing files: {str(e)}")
        


# Please provide source and targer directories before running the code
source_dir = "/path/to/source"
target_dir = "/path/to/target"
FileProcessor.copy_directory(source_dir, target_dir)


# Please provide the directory before you run the code
directory = "/path/to/directory"
extensions = [".txt", ".log"]
result = FileProcessor.process_files(directory, extensions)
