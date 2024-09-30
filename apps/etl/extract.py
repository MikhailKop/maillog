from config import settings


class MaillogExtractor:
    def __init__(self):
        self.log_file = self.get_file()

    def get_file(self):
        file = settings.file_path
        return file

    def read_file(self):
        result_data = []
        with open(self.log_file, 'r') as file:
            result_data = [line.split() for line in file]
        return result_data
