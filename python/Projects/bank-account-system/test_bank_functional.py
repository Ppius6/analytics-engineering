import unittest

from bank import BankAccount, SavingsAccount


class TestBankingWorkflow(unittest.TestCase):

    def test_complete_banking_workflow(self):
        # Customer opens accounts
        acc1 = BankAccount(1, "Pius", 0)
        acc2 = BankAccount(2, "Jane", 0)
        savings = SavingsAccount(3, "Mark", 0, 0.05)

        # Deposit money
        acc1.deposit(1000)
        acc2.deposit(500)

        # Transfer between accounts
        acc1.transfer(300, acc2)

        # Withdraw
        acc2.withdraw(100)

        # Save money and earn interest
        savings.deposit(2000)
        savings.apply_interest()

        # Verify the final state of everything
        self.assertEqual(acc1.balance, 700)
        self.assertEqual(acc2.balance, 700)
        self.assertEqual(savings.balance, 2100.0)


if __name__ == "__main__":
    unittest.main()
