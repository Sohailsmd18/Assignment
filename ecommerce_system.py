from typing import List, Dict
from datetime import datetime

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class Product:
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

class Order:
    def __init__(self, id: int, user_id: int, status: str, total: float):
        self.id = id
        self.user_id = user_id
        self.status = status
        self.total = total
        self.order_details: List[OrderDetail] = []

    def add_order_detail(self, order_detail: 'OrderDetail'):
        self.order_details.append(order_detail)

class OrderDetail:
    def __init__(self, id: int, order_id: int, product_id: int, quantity: int):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

class Payment:
    def __init__(self, id: int, order_id: int, amount: float, date: datetime):
        self.id = id
        self.order_id = order_id
        self.amount = amount
        self.date = date

class ECommerceSystem:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.products: Dict[int, Product] = {}
        self.orders: Dict[int, Order] = {}
        self.payments: Dict[int, Payment] = {}
        self.next_user_id = 1
        self.next_product_id = 1
        self.next_order_id = 1
        self.next_payment_id = 1
        self.next_order_detail_id = 1

    def create_user(self, name: str, email: str) -> User:
        user = User(self.next_user_id, name, email)
        self.users[user.id] = user
        self.next_user_id += 1
        return user

    def create_product(self, name: str, price: float, stock: int) -> Product:
        product = Product(self.next_product_id, name, price, stock)
        self.products[product.id] = product
        self.next_product_id += 1
        return product

    def create_order(self, user_id: int, products: List[Dict[int, int]]) -> Order:
        if user_id not in self.users:
            raise ValueError("User not found")

        total = 0
        order = Order(self.next_order_id, user_id, "pending", 0)
        self.next_order_id += 1

        for product_info in products:
            product_id = product_info['product_id']
            quantity = product_info['quantity']

            if product_id not in self.products:
                raise ValueError(f"Product with id {product_id} not found")

            product = self.products[product_id]
            if product.stock < quantity:
                raise ValueError(f"Insufficient stock for product {product.name}")

            product.stock -= quantity
            total += product.price * quantity

            order_detail = OrderDetail(self.next_order_detail_id, order.id, product_id, quantity)
            self.next_order_detail_id += 1
            order.add_order_detail(order_detail)

        order.total = total
        self.orders[order.id] = order
        return order

    def process_payment(self, order_id: int, amount: float) -> Payment:
        if order_id not in self.orders:
            raise ValueError("Order not found")

        order = self.orders[order_id]
        if order.total != amount:
            raise ValueError("Payment amount does not match order total")

        payment = Payment(self.next_payment_id, order_id, amount, datetime.now())
        self.next_payment_id += 1
        self.payments[payment.id] = payment

        order.status = "paid"
        return payment

    def update_order_status(self, order_id: int, status: str) -> None:
        if order_id not in self.orders:
            raise ValueError("Order not found")

        valid_statuses = ["pending", "paid", "shipped", "delivered", "cancelled"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {', '.join(valid_statuses)}")

        self.orders[order_id].status = status

# Example usage
if __name__ == "__main__":
    # Create an instance of the ECommerceSystem
    ecommerce = ECommerceSystem()

    # Create users
    user1 = ecommerce.create_user("Alice", "alice@example.com")
    user2 = ecommerce.create_user("Bob", "bob@example.com")

    # Create products
    product1 = ecommerce.create_product("Laptop", 999.99, 10)
    product2 = ecommerce.create_product("Mouse", 29.99, 50)

    # Create an order
    order = ecommerce.create_order(user1.id, [
        {"product_id": product1.id, "quantity": 1},
        {"product_id": product2.id, "quantity": 2}
    ])

    print(f"Order created: Total ${order.total:.2f}")

    # Process payment
    payment = ecommerce.process_payment(order.id, order.total)
    print(f"Payment processed: ${payment.amount:.2f}")

    # Update order status
    ecommerce.update_order_status(order.id, "shipped")
    print(f"Order status updated: {ecommerce.orders[order.id].status}")

    # Print final product stocks
    print(f"Laptop stock: {ecommerce.products[product1.id].stock}")
    print(f"Mouse stock: {ecommerce.products[product2.id].stock}")