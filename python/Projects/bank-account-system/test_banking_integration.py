import unittest
from bank import BankAccount, SavingsAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        BankAccount.all_accounts.clear()
        self.acc1 = BankAccount(1, "Pius", 1000)
        self.acc2 = BankAccount(2, "Jane", 500)
        self.savings = SavingsAccount(3, "Mark", 1000, 0.05)
        
    def test_all_accounts_tracks_all_created_accounts(self):
        # All three accounts should be registered
        self.assertEqual(len(BankAccount.all_accounts), 3)

    def test_savings_account_inherits_deposit(self):
        # SavingsAccount should be able to use BankAccount's deposit
        self.savings.deposit(500)
        self.assertEqual(self.savings.balance, 1500)

    def test_savings_account_inherits_withdraw(self):
        # SavingsAccount should be able to use BankAccount's withdraw
        self.savings.withdraw(200)
        self.assertEqual(self.savings.balance, 800)

    def test_transfer_correctly_updates_both_accounts(self):
        # Two BankAccount objects interacting via transfer
        self.acc1.transfer(300, self.acc2)
        self.assertEqual(self.acc1.balance, 700)  # sender reduced
        self.assertEqual(self.acc2.balance, 800)  # receiver increased

    def test_transfer_to_savings_account(self):
        # BankAccount transferring to a SavingsAccount
        self.acc1.transfer(500, self.savings)
        self.assertEqual(self.acc1.balance, 500)
        self.assertEqual(self.savings.balance, 1500)

    def test_deposit_then_transfer(self):
        # Chain of operations across two accounts
        self.acc1.deposit(500)               # acc1 = 1500
        self.acc1.transfer(700, self.acc2)   # acc1 = 800, acc2 = 1200
        self.assertEqual(self.acc1.balance, 800)
        self.assertEqual(self.acc2.balance, 1200)

    def test_interest_after_transfer(self):
        # Transfer into savings then apply interest
        self.acc1.transfer(1000, self.savings)   # savings = 2000
        self.savings.apply_interest()             # savings = 2000 + 100 = 2100
        self.assertEqual(self.savings.balance, 2100.0)

    def test_transfer_updates_both_accounts(self):
        r = self.acc1.transfer(300, self.acc2)
        self.assertEqual(self.acc1.balance, 700)
        self.assertEqual(self.acc2.balance, 800)


if __name__ == "__main__":
    unittest.main()
