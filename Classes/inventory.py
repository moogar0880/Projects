'''
Create an application which manages an inventory of
products. Create a product class which has a price,
id, and quantity on hand. Then create an inventory
class which keeps track of various products and can
sum up the inventory value.
'''

class Product(object):
  """docstring for Product"""
  def __init__(self, price, idNum, quantity):
    super(Product, self).__init__()
    self.price    = price
    self.id       = idNum
    self.quantity = quantity

  def sell(self,quantity):
    self.quantity -= quantity

  def recieve(self,quantity):
    self.quantity += quantity

class Inventory(object):
  """docstring for Inventory"""
  def __init__(self, products=None):
    super(Inventory, self).__init__()
    self.inventory = {}
    if products != None:
      for product in products:
        self.inventory[product.id] = product

  def add(self,product):
    self.inventory[product.id] = product

  def total(self):
    total = 0
    for key in self.inventory.keys():
      total += self.inventory[key].quantity * self.inventory[key].price
    return total

p = Product(10,0,10)
i = Inventory()
i.add(p)
print i.total()
