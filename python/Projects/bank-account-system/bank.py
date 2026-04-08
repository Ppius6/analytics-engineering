class BankAccount:
    all_accounts = []

    def __init__(self, account_id, owner_name, balance=0) -> None:
        self.account_id = account_id
        self.owner_name = owner_name
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Insufficient funds"

    def get_balance(self):
        return f"Account balance: {self.balance}"

    def transfer(self, amount, target_account):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount

            return f"Transferred {amount} to {target_account.owner_name}'s account"
        else:
            return "Insufficient funds for transfer"


class SavingsAccount(BankAccount):
    def __init__(self, account_id, owner_name, balance=0, interest_rate=0.05) -> None:
        super().__init__(account_id, owner_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
            return f"Interest applied. New balance: {self.balance}"
