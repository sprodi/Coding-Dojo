class User():
   
   def __init__(self, uname, initamount):
      self.username = uname
      self.balance = initamount
   
   def make_deposit(self, amount):
      self.balance += amount
      print(f"{self.username} Deposited ${amount}")
      return self

   def make_withdrawal(self, amount):
      if self.balance < amount:
            print(f"**Could not withdraw ${amount} due to insufficient funds.**")
      else:
         self.balance -= amount
         print(f"{self.username} Withdrew ${amount}")
      return self


   def transfer_money(self, other_user, amount):
      if self.balance < amount:
            print(f"**Could not transfer ${amount} to {other_user.username} due to insufficient funds.**")
      else:
         self.balance -= amount
         other_user.balance += amount
         print(f"{self.username} Transfered ${amount} to {other_user.username}")
      return self


   def display_user_balance(self):
      print(f"User: {self.username}, Balance: ${self.balance}")
      return self 
      

print()      
x = User("Sprodi", 0)
y = User("BentoBox", 0)
z = User("Parker", 0)

# Sprodi
x.make_deposit(500).make_deposit(200).make_deposit(50).make_withdrawal(150).display_user_balance()
print()

# BentoBox
y.make_deposit(1200).make_deposit(200).make_withdrawal(100).make_withdrawal(450).display_user_balance()
print()

# Parker
z.make_deposit(2500).make_withdrawal(300).make_withdrawal(100).make_withdrawal(100).display_user_balance()
print()

# Transfer
x.transfer_money(z, 600).display_user_balance()
z.display_user_balance()
