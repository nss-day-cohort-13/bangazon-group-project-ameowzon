from utility.utility import *


def delete_cart(file_name, user_id):
    """
    deletes all the line items associated with the cart ID passed in.
    =========
    Method Arguments: 1. file name of customer list to deserialize. 2. ID of user whose cart to clear.
    """

    customer_lib = deserialize(file_name)
    customer_lib[user_id].cart = {}
    serialize(file_name, customer_lib)


def build_cart_view(customer_id):
    """
    Queries the bangazon database to find:
    the order ID associated with the current customer where the payment is null (open order),
    the line items associated with that order ID,
    and the product names and prices associated with the line items.
    Since it's called within the menu printer utility, it also returns "true", which signals the menu printer to also print the prices.
    ======
    Method Argument: the ID of the current customer.
    Returns: list of tuples,
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
