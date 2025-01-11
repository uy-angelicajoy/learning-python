import os

class Order:
    def __init__(self):
        self.quantity = []
        self.price = 0
        
    def print_header(self, title): 
        os.system('cls')
        print(title)
        
    def product(self):
        self.print_header("Add Item Section")
        name = input("Item name: ")
        price = float(input(f"Enter the price of {name}: ₱"))
        qty = int(input(f"Enter the quantity of {name}: "))

        for item in self.items:
            if item['name'] == name:
                item['qty'] += qty
                self.total += price * qty

        self.items.append({'name': name, 'price': price, 'qty': qty})
        self.total += price * qty
        
        print(f"--{name} added successfully with {qty} units--")

    def display_order(self):
        self.print_header("Current Order")
        if not self.items:
            print('--Your order is empty--')
            return

        print(f"{'Item':<20}{'Qty':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)

        for idx, item in enumerate(self.items, start=1):
            total_price = item['price'] * item['qty']
            print(f"{idx}. {item['name']:<15} {item['qty']:<10} "
                  f"₱{item['price']:<10.2f} ₱{total_price:.2f}")

        print("-" * 50)
        print(f"Total Order Value: ₱{self.total:.2f}")
        
    def get_total(self):
        return self.price * self.quantity
        
