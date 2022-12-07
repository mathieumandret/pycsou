# coding utf-8

from datetime import datetime

RENT = 'SEPA ADL IMMOBILIER'
ELECTRICITY = 'SEPA EDF'
ISP = 'SEPA SFR FIXE ADSL'


class Operation:

    def __init__(
            self,
            creditor: str,
            operation_date: datetime.date,
            amount: float
    ):
        self.creditor = creditor
        self.operation_date = operation_date
        self.amount = amount

    def creditor_is_one_of(self, creditors: [str]) -> bool:
        for creditor in creditors:
            if creditor in self.creditor:
                return True
        return False

    def is_monthly_expense(self) -> bool:
        return self.creditor_is_one_of([RENT, ISP, ELECTRICITY])

    def __str__(self) -> str:
        return f'Creditor: {self.creditor},' \
               f' date: {self.operation_date}, amount: {self.amount}'
