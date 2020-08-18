class User():
   
   def __init__(self, uname, initamount):
      self.username = uname
      self.balance = initamount
   
   def make_deposit(self, amount):
      self.balance += amount
      print(f"{self.username} Deposited ${amount}")

   def make_withdrawal(self, amount):
      if self.balance < amount:
            print(f"**Could not withdraw ${amount} due to insufficient funds.**")
      else:
         self.balance -= amount
         print(f"{self.username} Withdrew ${amount}")


   def transfer_money(self, other_user, amount):
      if self.balance < amount:
            print(f"**Could not transfer ${amount} to {other_user.username} due to insufficient funds.**")
      else:
         self.balance -= amount
         other_user.balance += amount
         print(f"{self.username} Transfered ${amount} to {other_user.username}")



   def display_user_balance(self):
         return f"User: {self.username}, Balance: ${self.balance}"


print()      
x = User("Sprodi", 0)
y = User("BentoBox", 0)
z = User("Parker", 0)

# Sprodi
x.make_deposit(500)
x.make_deposit(200)
x.make_deposit(50)
x.make_withdrawal(150)

print(x.display_user_balance())
print()

# BentoBox
y.make_deposit(1200)
y.make_deposit(200)
y.make_withdrawal(100)
y.make_withdrawal(450)
print(y.display_user_balance())
print()

# Parker
z.make_deposit(2500)
z.make_withdrawal(300)
z.make_withdrawal(100)
z.make_withdrawal(100)
print(z.display_user_balance())
print()

# Transfer
x.transfer_money(z, 600)
print(x.display_user_balance())
print(z.display_user_balance())
