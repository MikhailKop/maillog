import re
from datetime import datetime

from models import Log, Message


class TransformData:
    def __init__(self, input_data: list):
        self.data = input_data

    def str_to_date(self, str_date):
        date = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
        return date

    def get_id(self, row: list):
        for elem in row:
            result = re.match(r'id=', elem)
            if result:
                id = elem[3:]
                return id
        return 'id not found'

    def get_address(self, row: list):
        if (len(row)) > 4 and (row[3] == '=>' or '->' or '**' or '=='):
            return row[4]

    def get_str(self, row: list):
        result = ''
        for num in range(2, len(row)):
            result += str(row[num]) + ' '
        return result[:-1]

    def transform(self):
        log_data = []
        message_data = []
        """Pydantyc models are used for validation"""
        for row in self.data:
            if row[3] == '<=':
                message_data.append(
                    Message(
                        created=self.str_to_date(row[0] + ' ' + row[1]),
                        id=self.get_id(row),
                        int_id=row[2],
                        str_=self.get_str(row),
                        )
                )

            else:
                log_data.append(
                    Log(
                        created=self.str_to_date(row[0] + ' ' + row[1]),
                        int_id=row[2],
                        str_=self.get_str(row),
                        address=self.get_address(row),
                        )
                )
        return log_data, message_data
