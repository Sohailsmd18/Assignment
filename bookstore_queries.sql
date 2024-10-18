-- 1. Top 5 customers who purchased the most books over the last year
SELECT c.customer_id, c.name, SUM(od.quantity) as total_books
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.customer_id, c.name
ORDER BY total_books DESC
LIMIT 5;

-- 2. Total revenue generated from book sales by each author
SELECT b.author, SUM(b.price * od.quantity) as total_revenue
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.author
ORDER BY total_revenue DESC;

-- 3. Books ordered more than 10 times, with total quantity ordered
SELECT b.book_id, b.title, SUM(od.quantity) as total_ordered
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.book_id, b.title
HAVING total_ordered > 10
ORDER BY total_ordered DESC;
    