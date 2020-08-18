class BankAccount:

   def __init__(self, int_rate, balance=0):
      self.interest_rate = int_rate
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
      print(f"Deposited ${amount}")
      return self

   def withdraw(self, amount):
      if self.balance < amount:
         self.balance -= 5
         print(f"**Insufficient funds: Charging a $5 fee.**")
      else:
         self.balance -= amount
         print(f"Withdrew ${amount}")
      return self

   def display_account_info(self):
      print(f"====================\nBalance: ${round(self.balance, 2)}\nIntrest Rate: ${self.interest_rate}\n====================")
      return self

   def yield_interest(self):
      if self.balance > 0:
         self.balance += self.interest_rate * self.balance
      else: 
         self.balance = self.balance
      return self

x = BankAccount(.0003, 200)
y = BankAccount(.0006)

print(f"\n*** First Account ***")
x.display_account_info().deposit(100).deposit(150).deposit(150).withdraw(50).yield_interest().display_account_info()
print()
print(f"\n*** Second Account ***")
y.display_account_info().deposit(200).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()
print()


