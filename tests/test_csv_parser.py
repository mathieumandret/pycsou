import datetime
from operation import Operation

from parsers.CsvParser import CsvParser


class TestCsvParser:

    @staticmethod
    def assert_operation_equal(
            operation: Operation,
            creditor: str,
            amount: float,
            date: datetime.datetime
    ):
        assert operation.creditor == creditor
        assert operation.amount == amount
        assert operation.operation_date == date

    def test(self):
        parser = CsvParser()
        with open('assets/input.csv') as file:
            operations = parser.parse_file(file)
            #  The test file contains 10 operations
            assert len(operations) == 10

            walmart = operations[0]
            self.assert_operation_equal(
                walmart,
                creditor='Walmart',
                amount=-50,
                date=datetime.datetime(
                    day=7,
                    month=10,
                    year=2022
                )
            )

            spotify = operations[7]
            self.assert_operation_equal(
                spotify,
                creditor='Spotify',
                amount=-35,
                date=datetime.datetime(
                    day=1,
                    month=11,
                    year=2022
                )
            )
