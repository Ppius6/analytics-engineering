import unittest
from bank import BankAccount, SavingsAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc1 = BankAccount(1, "Pius", 1000)
        self.acc2 = BankAccount(2, "Jane", 500)

    def test_deposit_increases_balance(self):
        result = self.acc1.deposit(200)
        self.assertEqual(self.acc1.balance, 1200)
        self.assertEqual(result, "Deposited 200. New balance: 1200")

    def test_withdraw_decreases_balance(self):
        result = self.acc2.withdraw(200)
        self.assertEqual(self.acc2.balance, 300)
        self.assertEqual(result, "Withdrew 200. New balance: 300")

    def test_negative_withdraw_declined(self):
        result = self.acc1.withdraw(1100)
        self.assertEqual(result, "Insufficient funds")

    def test_get_balance(self):
        self.assertEqual(self.acc1.balance, 1000)
        result = self.acc1.get_balance()
        self.assertEqual(result, "Account balance: 1000")

    def test_failed_transfer(self):
        result = self.acc1.transfer(1300, self.acc2)
        self.assertEqual(result, "Insufficient funds for transfer")


class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        self.savings = SavingsAccount(3, "Mark", 1000, 0.05)

    def test_apply_interest(self):
        result = self.savings.apply_interest()
        self.assertEqual(self.savings.balance, 1050.0)
        self.assertEqual(result, "Interest applied. New balance: 1050.0")


if __name__ == "__main__":
    unittest.main()
