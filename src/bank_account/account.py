class BankAccount:
    """
    Represents a simple bank account.

    This class allows basic banking operations such as depositing money,
    withdrawing money, and checking the current balance.
    """

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Initialize a new bank account.

        Args:
            owner (str): Name of the account holder.
            balance (float, optional): Initial balance of the account.
                Defaults to 0.0.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the bank account.

        Args:
            amount (float): Amount to be deposited.

        Raises:
            ValueError: If the deposit amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the bank account.

        Args:
            amount (float): Amount to be withdrawn.

        Raises:
            ValueError: If the withdrawal amount is less than or equal to zero.
            ValueError: If the withdrawal amount exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Get the current balance of the bank account.

        Returns:
            float: The current account balance.
        """
        return self.balance
