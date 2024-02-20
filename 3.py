from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass  # Complete this method in subclasses

# Example subclass
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal cancelled.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. Remaining balance: ${self.balance}")

# Example usage:
savings_account = SavingsAccount(balance=1000)
savings_account.withdraw(500)  # Successful withdrawal
savings_account.withdraw(800)  # Insufficient funds
