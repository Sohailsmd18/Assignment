from typing import List, Dict, Tuple

class Product:
    def __init__(self, id: int, name: str, stock: int):
        self.id = id
        self.name = name
        self.stock = stock

class Order:
    def __init__(self, id: int, product_id: int, quantity: int):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity

def process_orders(products: Dict[int, Product], orders: List[Order], threshold: int = 10) -> List[Tuple[int, str, int]]:
    alerts = []
    
    for order in orders:
        if order.product_id not in products:
            raise ValueError(f"Product with id {order.product_id} not found")
        
        product = products[order.product_id]
        
        if product.stock < order.quantity:
            raise ValueError(f"Insufficient stock for product {product.name}")
        
        product.stock -= order.quantity
        
        if product.stock < threshold:
            alerts.append((product.id, product.name, product.stock))
    
    return alerts

def restock_items(products: Dict[int, Product], restock_list: List[Tuple[int, int]]) -> None:
    for product_id, quantity in restock_list:
        if product_id not in products:
            raise ValueError(f"Product with id {product_id} not found")
        
        products[product_id].stock += quantity

# Example usage
if __name__ == "__main__":
    # Initialize products
    products = {
        1: Product(1, "Book", 50),
        2: Product(2, "Pen", 100),
        3: Product(3, "Notebook", 30)
    }

    # Create some orders
    orders = [
        Order(1, 1, 20),
        Order(2, 2, 50),
        Order(3, 3, 25)
    ]

    # Process orders
    try:
        alerts = process_orders(products, orders)
        print("Orders processed successfully")
        if alerts:
            print("Restocking alerts:")
            for product_id, name, stock in alerts:
                print(f"Product {name} (ID: {product_id}) has low stock: {stock}")
    except ValueError as e:
        print(f"Error processing orders: {e}")

    # Restock items
    restock_list = [(1, 30), (3, 20)]
    try:
        restock_items(products, restock_list)
        print("Items restocked successfully")
    except ValueError as e:
        print(f"Error restocking items: {e}")

    # Print updated stock levels
    print("Updated stock levels:")
    for product in products.values():
        print(f"{product.name}: {product.stock}")