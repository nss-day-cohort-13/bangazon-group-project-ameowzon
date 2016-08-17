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


def build_cart_view(customer_id):
    """
    Queries the bangazon database to find:
    -the order ID associated with the current customer where the payment is null (open order),
    -the line items associated with that order ID,
    -and the product names and prices associated with each matching line item.
    Since it's called within the menu printer utility, it returns "true", which signals the menu printer to print the prices as well as the product names.
    ======
    Method Argument: the ID of the current customer.
    Returns: list of tuples, "true"
    """

    with sqlite3.connect("bangazon.db") as database:
            db = database.cursor()

            db.execute("""SELECT p.Name, p.price
                            FROM Product p
                            INNER JOIN
                                (SELECT li.ProductId
                                FROM LineItem li
                                INNER JOIN
                                    (SELECT o.orderId currentOrder
                                    FROM orders o
                                    INNER JOIN customer c ON c.CustomerId = o.CustomerId
                                    WHERE c.CustomerId = ?
                                    AND o.PaymentID = Null) cart
                                ON cart.currentOrder = li.orderId) cartItems
                            ON p.ProductId = cartItems.productId""", (customer_id,))
            return db.fetchall(), True
