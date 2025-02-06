class Order:
    def __init__(self):
        self.total = 0  # Initialize total order value to 0

    def place_order(self, amount):
        if amount <= 0:
            raise ValueError("Order amount must be positive.")  # Raise error for negative order
        self.total += amount  # Add amount to total
        print(f"Order of {amount} placed successfully. Current total: {self.total}")

    def apply_discount(self, discount):
        if discount < 0:
            raise ValueError("Discount cannot be negative.")  # Raise error for negative discount
        if discount > self.total:
            raise ValueError("Discount cannot be greater than total order value.")  # Prevent excessive discount
        self.total -= discount  # Subtract discount from total
        print(f"Discount of {discount} applied successfully. Current total: {self.total}")

# Main program
order = Order()

try:
    order_amount = int(input())  # Get order amount
    order.place_order(order_amount)  # Place order
except ValueError as e:
    print(f"Order failed. {e}")

try:
    discount_amount = int(input())  # Get discount amount
    order.apply_discount(discount_amount)  # Apply discount
except ValueError as e:
    print(f"Discount failed. {e}")
