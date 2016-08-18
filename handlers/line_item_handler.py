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
        db.execute("INSERT INTO LineItem (OrderId, ProductId) VALUES (?, ?)", (order_id, product_id))
        conn.commit()

    return


def return_report_line_items(input_file='bangazon.db'):
    """
    Returns a list of line items with orders that have been completed.
    """

    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()
        db.execute("SELECT li.* FROM LineItem li, Orders o WHERE li.OrderID == o.OrderID AND o.PaymentID != NULL")
        conn.commit()

    return db.fetchall()
