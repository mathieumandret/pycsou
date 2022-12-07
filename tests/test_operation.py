import datetime
from operation import Operation


def test_to_string():
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

    expected_str =\
        f'Creditor: {creditor},' \
        f' date: 2022-09-21 20:59:03, amount: 12.1'

    assert expected_str == operation.__str__()
