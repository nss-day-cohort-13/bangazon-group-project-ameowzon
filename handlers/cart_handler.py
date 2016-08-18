from utility.utility import *
import sqlite3


def delete_cart(customer_id):
    """
    Deletes all the line item rows associated with the orderID of the unpaid order associated with the current customer.
    =========
    Method Argument: the ID of the current customer.
    Returns: an empty list, so if the customer is currently shopping they can see the 'cart is empty' message.
    """
    with sqlite3.connect("bangazon.db") as database:
        db = database.cursor()

        db.execute("""DELETE li.*
                        FROM LineItem li,
                            (SELECT o.orderId currentOrder
                            FROM orders o
                            INNER JOIN customer c ON c.CustomerId = o.CustomerId
                            WHERE c.CustomerId = ?
                            AND o.PaymentID = Null) cart
                        WHERE cart.currentOrder = li.orderId""", (customer_id,))
        database.commit()
        return []


def build_cart_view(order_id):
    """
    Queries the bangazon database to find:
    -the line items associated with a passed-in order ID,
    -and the product names and prices associated with each matching line item.
    ======
    Method Argument: the ID of the current order.
    Returns: list of tuples
    """
    with sqlite3.connect("bangazon.db") as database:
            db = database.cursor()

            db.execute("""SELECT p.Name, COUNT(cartItems.ProductId), SUM(p.price)
                            FROM Product p
                            INNER JOIN
                                (SELECT li.ProductId
                                FROM LineItem li
                                WHERE li.orderId = ?) cartItems
                            ON p.ProductId = cartItems.productId
                            GROUP BY p.ProductId""", (order_id,))
            return db.fetchall()


def check_if_cart_exists(customer_id):
    """
    Queries the bangazon database to find:
    -the order ID associated with a passed-in customer ID,
    -where the payment is Null(meaning the order is a 'cart', or unpaid.)
    ========
    Method Argument: the ID of the current customer.
    Returns: tuple with a string in it.
    """
    with sqlite3.connect("bangazon.db") as database:
            db = database.cursor()

            db.execute("""SELECT o.OrderID
                            FROM Orders o
                            WHERE o.CustomerID = ?
                            AND o.PaymentID IS NULL""", (customer_id,))
            cart = db.fetchone()
            return cart[0]
