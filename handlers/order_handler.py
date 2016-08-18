from objects.order_object import *
import sqlite3
import curses


def new_order(cust_key):
    """
    Create new order row in db, return order id

    Args-customer id
    """
    with sqlite3.connect("bangazon.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Orders (PaymentId, CustomerId) VALUES (?,?)", (None, cust_key))
        conn.commit()
        c.execute("SELECT o.OrderId FROM Orders o WHERE o.CustomerId=? AND o.PaymentId=?", (cust_key, None))
        order_id = c.fetchone()
        print(order_id[0])
        return order_id[0]


def add_payment_to_order(cust_key, payment_id):
    """
    Adds a payment method to an open order

    Args-customer id with open order, payment id of payment method
    """
    with sqlite3.connect("bangazon.db") as conn:
        c = conn.cursor()
        c.execute("UPDATE Orders SET PaymentId=? WHERE CustomerId=? AND PaymentId IS ?", (payment_id, cust_key, None))
        conn.commit()


def get_last_order_for_menu():
    """
    Returns the most recently purchased item to the Meow show purchased menu
    """

    with sqlite3.connect("bangazon.db") as conn:
        db = conn.cursor()
        db.execute("""SELECT p.* FROM Orders o, LineItem li, Product p WHERE o.OrderId == (SELECT o.OrderId
            FROM Orders o ORDER BY OrderId DESC LIMIT 1) AND li.OrderId == (SELECT o.OrderId
            FROM Orders o ORDER BY OrderId DESC LIMIT 1) AND p.ProductID == li.ProductID""")

        return db.fetchall()
