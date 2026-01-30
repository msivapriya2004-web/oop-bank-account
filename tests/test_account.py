import pytest
from src.bank_account.account import BankAccount


# -------------------------------
# Account Creation
# -------------------------------

def test_initial_balance_default():
    account = BankAccount("Alice")
    assert account.get_balance() == 0.0


def test_initial_balance_with_value():
    account = BankAccount("Bob", 100)
    assert account.get_balance() == 100


# -------------------------------
# Deposit Tests
# -------------------------------

def test_deposit_valid_amount():
    account = BankAccount("Alice", 100)
    account.deposit(50)
    assert account.get_balance() == 150


def test_deposit_zero_raises_error():
    account = BankAccount("Alice", 100)
    with pytest.raises(ValueError):
        account.deposit(0)


def test_deposit_negative_raises_error():
    account = BankAccount("Alice", 100)
    with pytest.raises(ValueError):
        account.deposit(-10)


def test_multiple_deposits():
    account = BankAccount("Alice", 0)
    account.deposit(100)
    account.deposit(200)
    assert account.get_balance() == 300


# -------------------------------
# Withdraw Tests
# -------------------------------

def test_withdraw_valid_amount():
    account = BankAccount("Dave", 200)
    account.withdraw(50)
    assert account.get_balance() == 150


def test_withdraw_exact_balance():
    account = BankAccount("Dave", 100)
    account.withdraw(100)
    assert account.get_balance() == 0


def test_withdraw_insufficient_balance():
    account = BankAccount("Dave", 50)
    with pytest.raises(ValueError):
        account.withdraw(100)


def test_withdraw_zero_raises_error():
    account = BankAccount("Dave", 100)
    with pytest.raises(ValueError):
        account.withdraw(0)


def test_withdraw_negative_raises_error():
    account = BankAccount("Dave", 100)
    with pytest.raises(ValueError):
        account.withdraw(-20)


# -------------------------------
# Combined Operations
# -------------------------------

def test_deposit_then_withdraw():
    account = BankAccount("Eve", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.get_balance() == 120
