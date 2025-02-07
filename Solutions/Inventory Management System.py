class Inventory:
    def __init__(self):
        self.products = {}  # Dictionary to store product names and their quantities

    def add_product(self, product_name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")  # Raise error for negative quantity
        if product_name in self.products:
            self.products[product_name] += quantity  # Update quantity if product exists
        else:
            self.products[product_name] = quantity  # Add new product
        print(f"{quantity} {product_name} added to inventory. Current quantity: {self.products[product_name]}")

    def remove_product(self, product_name, quantity):
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found in inventory.")  # Error if product not found
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")  # Raise error for negative quantity
        if self.products[product_name] < quantity:
            raise ValueError(f"Not enough {product_name} in inventory to remove {quantity}.")  # Error if removing more than available
        self.products[product_name] -= quantity  # Remove quantity
        print(f"{quantity} {product_name} removed from inventory. Current quantity: {self.products[product_name]}")

# Main program
inventory = Inventory()

try:
    product_name, quantity = input().split()
    inventory.add_product(product_name, int(quantity))  # Add product
except ValueError as e:
    print(f"Addition failed. {e}")

try:
    product_name, quantity = input().split()
    inventory.remove_product(product_name, int(quantity))  # Remove product
except ValueError as e:
    print(f"Removal failed. {e}")
