class Store:
   
   def __init__(self, name, products):
      self.store = name
      self.products = products

   def add_product(self, new_product):
      self.products.append(new_product)

   def sell_product(self, id):
      print(f"Removed {self.products[id]}")
      Products.print_info(Paper) # THIS IS BROKEN - sell_product(self, id) section
      self.products.pop(id)

class Products:

   def __init__(self, name, price, category):
      self.name = name
      self.price = price
      self.category = category

   def update_price(self, percent_change, is_increased):
      if is_increased == True:
         self.price *= percent_change
         return self.price
      else:
         if is_increased == False:
            self.price /= percent_change
            return self.price

   def print_info(self):
      print(f"\nProduct Name: {self.name}\nProduct Price: ${self.price}\nProduct Category: {self.category}\n")

store = Store(
   "Sean Store",
   []
)

Rock = Products("Rock", 20, "Trash")
Paper = Products("Paper", 40, "Office")

store.add_product("Rock")
print(f"\nStore Products: {store.products}\n")
print(f"{Rock.name} Original Price: {Rock.price}")
Rock.update_price(2, True)
print(f"{Rock.name} New Price: {Rock.price}")
Rock.print_info()
store.add_product("Paper")
print(f"Store Products: {store.products}\n")
store.sell_product(1)
print(f"Store Products: {store.products}\n")
