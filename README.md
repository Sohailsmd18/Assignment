# E-commerce and Bookstore System

This project contains implementations for an e-commerce system, an inventory management system, and SQL queries for a bookstore database.

## Contents

1. `ecommerce_system.py`: Contains class stubs for the e-commerce system components.
2. `inventory_management.py`: Implements inventory management functions.
3. `bookstore_queries.sql`: SQL queries for the online bookstore database.

## How to Run

### E-commerce System

The `ecommerce_system.py` file contains class stubs and doesn't require execution. It serves as a foundation for further development.

### Inventory Management System

To run the inventory management system:

1. Ensure you have Python 3.6+ installed.
2. Run the following command:

```
python inventory_management.py
```

This will execute the example usage provided in the script.

### Bookstore Queries

The SQL queries in `bookstore_queries.sql` can be executed in any SQL database management system that supports standard SQL syntax. Make sure to create the necessary tables (Customers, Books, Orders, OrderDetails) before running the queries.

## Assumptions

1. E-commerce System:
   - Each order is associated with a single user.
   - An order can have multiple products (represented by OrderDetail).
   - A payment is associated with a single order.

2. Inventory Management:
   - Product IDs are unique.
   - The stock threshold for alerts is set to 10 by default but can be changed.

3. Bookstore Queries:
   - The database schema is as provided in the problem statement.
   - The current date is used as a reference point for the "last year" calculation.

## Notes

- The e-commerce system implementation is a basic structure and would need further development for a complete system.
- The inventory management system includes error handling for common issues like insufficient stock or invalid product IDs.
- The SQL queries include indexing recommendations for performance optimization.