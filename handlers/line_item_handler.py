from objects.line_item_object import *
from utility.utility import *
import sqlite3


def generate_new_line_item(order_id, product_id, input_file='bangazon.db'):
    """
    Creates a new line item entry into LineItem table.
    ===================
    input-file - database file
    order_id - id that line item is associated with
    product_id - id that line item associated with
    """

    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()
        db.execute("INSERT INTO LineItem (OrderId, ProductId) VALUES (order_id, product_id)")
        db.commit()

    return


def return_report_line_items(input_file='bangazon.db'):
    """
    Returns a list of line items with orders that have been completed.
    """

    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()
        db.execute("""
SELECT
    p.ProductId,
    p.Name,
    COUNT(p.ProductId) 'Units Sold',
    COUNT(DISTINCT c.CustomerId) 'Customers',
    SUM(p.Price) 'Revenue'
FROM Product p
INNER JOIN LineItem l ON l.ProductId = p.ProductId
INNER JOIN Orders o ON l.OrderId = o.OrderId
INNER JOIN Customer c ON o.CustomerId = c.CustomerId
WHERE o.PaymentId IS NOT NULL
GROUP BY p.ProductId
            """)
        db.commit()

    return db.fetchall()
