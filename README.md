
# OOP Bank Account 🏦

A simple Object-Oriented Python project that models a bank account with basic operations such as deposit, withdrawal, and balance inquiry.  
The project follows clean OOP principles, includes unit tests, and enforces high test coverage using GitHub Actions.

---

## 📌 Features

- Create a bank account with an owner and initial balance
- Deposit money into the account
- Withdraw money with validation checks
- Prevent invalid transactions (negative amounts, insufficient balance)
- Retrieve current account balance
- Fully unit-tested with pytest
- Enforced 90%+ test coverage

---

## 📁 Project Structure

oop-bank-account/
│
├── src/
│   └── bank_account/
│       ├── **init**.py
│       └── account.py
│
├── tests/
│   └── test_account.py
│
├── pyproject.toml
├── README.md
└── .github/
└── workflows/
└── python.yml


---

## 🧑‍💻 BankAccount Class

### Available Methods

| Method | Description |
|------|------------|
| `deposit(amount)` | Deposits a positive amount into the account |
| `withdraw(amount)` | Withdraws money if sufficient balance exists |
| `get_balance()` | Returns the current account balance |

---

## 🧪 Running Tests

Run unit tests:

```bash
pytest
````

---

## 📊 Test Coverage

Run tests with coverage:

```bash
pytest --cov=src/bank_account --cov-report=term-missing
```

Generate HTML coverage report:

```bash
pytest --cov=src/bank_account --cov-report=html
```

Open the report:

```
htmlcov/index.html
```

---

## ✅ Continuous Integration

This project uses GitHub Actions to automatically:

* Run unit tests on every push
* Check test coverage
* Fail the build if coverage is below 90%

---

## 🛠 Technologies Used

* Python 3.10
* pytest
* pytest-cov
* Poetry
* GitHub Actions

---

## 🎯 Learning Outcomes

* Object-Oriented Programming in Python
* Writing clean, testable code
* Unit testing with pytest
* Measuring and enforcing test coverage
* Python packaging using src layout
* CI/CD fundamentals with GitHub Actions

---


