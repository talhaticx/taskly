import os
import shutil

class DataFile:
    def __init__(self, path, default_path):

        # Define the path to the local default settings file
        self.default_file = os.path.join(os.path.dirname(__file__), default_path)

        # Define the path to the configuration file
        self.file_path = os.path.expanduser(path)

    def get_data(self):
        if not os.path.exists(self.file_path):
            self.__set_default_file()
        
        # Load and return the configuration
        data = {}
        with open(self.file_path, 'r') as f:
            exec(f.read(), data)
        
        return data

    def __set_default_file(self):
        if not os.path.exists(self.file_path):
            self.__copy_default_settings()

    def reset_default_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Copy the default settings file to self.file_path
        self.__copy_default_settings()

    def __copy_default_settings(self):
        # Ensure the directory exists
        config_dir = os.path.dirname(self.file_path)
        os.makedirs(config_dir, exist_ok=True)

        # Copy the default settings file to self.file_path
        shutil.copyfile(self.default_file, self.file_path)