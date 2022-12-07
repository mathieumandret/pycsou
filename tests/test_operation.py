import datetime
from operation import Operation


class TestOperation:

    def test_to_string(self):
        creditor = 'Creditor'
        amount = 12.1
        date = datetime.datetime(
            year=2022,
            month=9,
            day=21,
            hour=20,
            minute=59,
            second=3
        )

        operation = Operation(
            creditor=creditor,
            amount=amount,
            operation_date=date
        )

        expected_str = \
            f'Creditor: {creditor},' \
            f' date: 21/09/2022, amount: 12.1'

        assert expected_str == operation.__str__()

    def test_is_one_of_with_empty_list_is_false(self):
        operation = Operation('creditor', datetime.date.today(), 0)
        assert not operation.creditor_is_one_of([])

    def test_is_one_of_with_different_creditor_is_false(self):
        operation = Operation('A', datetime.date.today(), 0)
        assert not operation.creditor_is_one_of(['B', 'C'])

    def test_is_one_of_with_creditor_is_true(self):
        operation = Operation('B', datetime.date.today(), 0)
        assert operation.creditor_is_one_of(['B', 'C'])
