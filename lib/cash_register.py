#!/usr/bin/env python3

class CashRegister:
    
    
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = {}

    def add_item(self, title:str, price:int, quantity=1):
        self.total += (quantity * price)
        for i in range(quantity):
          self.items.append(title)
        self.last_transaction = {
           "title": title,
           "price": price,
           "quantity": quantity
        }

    def apply_discount(self):
        self.total = self.total - self.total * 0.2
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
          print(f"After the discount, the total comes to ${int(self.total)}.")
    def void_last_transaction(self):
       for i in range(self.last_transaction["quantity"]):
          self.total -= self.last_transaction["price"]
          self.items.pop()