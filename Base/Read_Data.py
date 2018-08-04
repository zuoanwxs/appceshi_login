
import yaml, os

class Read_Data:
    def __init__(self, file_name):
        self.file_path ="./Data" + os.sep + file_name

    def get_data(self):

        with open(self.file_path, "r") as f:

            return yaml.load(f)