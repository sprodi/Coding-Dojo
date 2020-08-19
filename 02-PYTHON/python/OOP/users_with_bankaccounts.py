class BankAccount:

   def __init__(self, int_rate, balance=0):
      self.interest_rate = int_rate
      self.balance = balance

   def deposit(self, amount):
      self.balance += amount
      print(f"Deposited ${amount}")
      return self

   def withdraw(self, amount):
      amount_after_withdraw = self.balance - amount
      if amount_after_withdraw < 0:
         print(f"**Insufficient funds: Charging a $5 fee.**")
         self.balance -= 5
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

class User:
   def __init__(self, name, email):
      self.name = name
      self.email = email
      self.account = BankAccount(int_rate=0.02, balance=0)
   
   def deposit(self):
      self.account.deposit(100)
      return self
   
   def withdraw(self):
      self.account.withdraw(25)
      return self

   def display_user_balance(self):
      self.account.display_account_info()

   def interest_rate(self):
      self.account.yield_interest()
      return self

x = User("Sean", "seanprodi@gmail.com")
x.deposit().withdraw().interest_rate().display_user_balance()