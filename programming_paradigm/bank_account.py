class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Returns True if successful."""
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Print the current balance in a friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
