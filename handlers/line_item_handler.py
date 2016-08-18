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
        db.execute("INSERT INTO LineItem (OrderId, ProductId) VALUES (?, ?)", (order_id, product_id))
        conn.commit()

    return


def return_report_line_items(input_file='bangazon.db'):
    """
    Returns a list of line items with orders that have been completed.
    """

    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()
        db.execute("""
            SELECT
                p.Name,
                COUNT(DISTINCT o.OrderId) 'Orders',
                COUNT(DISTINCT c.CustomerId) 'Customers',
                SUM(p.Price) 'Revenue'
            FROM Product p
            INNER JOIN LineItem l ON l.ProductId = p.ProductId
            INNER JOIN Orders o ON l.OrderId = o.OrderId
            INNER JOIN Customer c ON o.CustomerId = c.CustomerId
            WHERE o.PaymentId is not NULL
            GROUP BY p.Name
                        """)
        conn.commit()

    return db.fetchall()

def return_report_totals(input_file='bangazon.db'):
    """
    Returns the totals for the last line of the popularity report
    """
    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()
        db.execute("""
            SELECT
                COUNT(DISTINCT TotalOrders) 'Orders',
                COUNT(DISTINCT TotalCustomers) 'Customers',
                SUM(TotalRevenue) 'Revenue'
            FROM
                (SELECT
                    p.Name,
                    o.OrderId as TotalOrders,
                    c.CustomerId as TotalCustomers,
                    p.Price as TotalRevenue
                FROM Product p
                INNER JOIN LineItem l ON l.ProductId = p.ProductId
                INNER JOIN Orders o ON l.OrderId = o.OrderId
                INNER JOIN Customer c ON o.CustomerId = c.CustomerId
                WHERE o.PaymentId is not NULL
                ORDER BY p.Name)
                        """)
        conn.commit()

    return db.fetchall()
