# coding: utf-8

from parsers.CsvParser import CsvParser
from operation import Operation

from collections import defaultdict


def sort_by_month(operations: [Operation]):
    by_date = defaultdict(list)

    for op in operations:
        m = op.operation_date.month
        y = op.operation_date.year

        by_date[(m, y)].append(op)

    return by_date


def get_operations_from_file(filename: str) -> [Operation]:
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        parser = CsvParser()
        return parser.parse_file(file)


def main():
    operations = get_operations_from_file('input.csv')
    by_month = sort_by_month(operations)
    print(by_month)


if __name__ == '__main__':
    main()
