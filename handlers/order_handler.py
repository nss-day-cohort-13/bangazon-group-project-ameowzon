import sqlite3

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
