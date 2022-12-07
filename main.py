#coding: utf-8
import csv
from datetime import datetime
from functools import reduce
from collections import defaultdict

DATE_FORMAT = '%d/%m/%Y'

RENT='SEPA ADL IMMOBILIER'
ELECTRICITY='SEPA EDF'
ISP='SEPA SFR FIXE ADSL'


class Operation:

    def __init__(self, creditor: str, operation_date: datetime.date, amount: float):
        self.creditor = creditor
        self.operation_date = operation_date
        self.amount = amount

    def creditor_is_one_of(self, creditors: [str]) -> bool:
        for creditor in creditors:
            if creditor in self.creditor:
                return True
        return False

    def is_monthly_expense(self) -> bool:
        return self.creditor_is_one_of([RENT, ISP, ELECTRICITY]);

    def __str__(self) -> str:
        return f'Creditor={self.creditor}, date: {self.operation_date}, amount: {self.amount}'


def sort_by_month(operations: [Operation]):
    by_date = defaultdict(list)

    for op in operations:
        m = op.operation_date.month
        y = op.operation_date.year

        by_date[(m,y)].append(op)

    return by_date


def row_to_operation(row) -> Operation:
    raw_date = row[0];
    raw_amount = row[1];
    creditor = row[4];

    date = datetime.strptime(raw_date, DATE_FORMAT)
    amount = float(raw_amount.replace(',', '.'))
    return Operation(creditor, date, amount)

def parse_operations(file) -> [Operation]:
    reader = csv.reader(file, delimiter=';')
    ops = []
    for row in reader:
        if len(row) < 5:
            continue
        operation = row_to_operation(row)
        if (operation.is_monthly_expense()):
            ops.append(row_to_operation(row))
    return ops

def get_operations_from_file(filename: str) -> [Operation]:
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        return parse_operations(file)


operations = get_operations_from_file('input.csv')
by_month = sort_by_month(operations)

for (m, y), op in by_month.items():
    print(f'{m}-{y}')
    for o in op:
        print(o)
