import os
import shutil

class DataFile:
    def __init__(self, file):

        # Define the path to the local default settings file
        self.default_file = os.path.join(os.path.dirname(__file__), 'setting.py')

        # Define the path to the configuration file
        self.config_path = os.path.expanduser('~/.config/todos/setting.py')

    def get_config(self):
        if not os.path.exists(self.config_path):
            self.set_default_config()
        
        # Load and return the configuration
        config = {}
        with open(self.config_path, 'r') as f:
            exec(f.read(), config)

        # Filter out only the 'settings' dictionary
        if 'settings' in config:
            return config['settings']
        else:
            return {}

    def set_default_config(self):
        if not os.path.exists(self.config_path):
            self.copy_default_settings()

    def reset_default_config(self):
        if os.path.exists(self.config_path):
            os.remove(self.config_path)

        # Copy the default settings file to self.config_path
        self.copy_default_settings()

    def copy_default_settings(self):
        # Ensure the directory exists
        config_dir = os.path.dirname(self.config_path)
        os.makedirs(config_dir, exist_ok=True)

        # Copy the default settings file to self.config_path
        shutil.copyfile(self.default_file, self.config_path)