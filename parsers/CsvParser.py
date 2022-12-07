# coding: utf-8

import csv

from operation import Operation
from datetime import datetime

DATE_FORMAT = '%d/%m/%Y'


class CsvParser:

    @staticmethod
    def row_to_operation(row: [str]) -> Operation:
        raw_date = row[0]
        raw_amount = row[1]
        creditor = row[4]

        date = datetime.strptime(raw_date, DATE_FORMAT)
        amount = float(raw_amount.replace(',', '.'))
        return Operation(creditor, date, amount)

    def parse_file(self, file) -> [Operation]:
        reader = csv.reader(file, delimiter=';')
        ops = list()
        for row in reader:
            if len(row) < 5:
                continue
            operation = self.row_to_operation(row)
            ops.append(operation)
        return ops
