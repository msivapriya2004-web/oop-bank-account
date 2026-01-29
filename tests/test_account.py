import pytest
from src.bank_account.account import BankAccount


def test_initial_balance():
    account = BankAccount("Alice")
    assert account.get_balance() == 0.0


def test_withdraw_insufficient_balance():
    account = BankAccount("Dave", 50)
    with pytest.raises(ValueError):
        account.withdraw(100)
