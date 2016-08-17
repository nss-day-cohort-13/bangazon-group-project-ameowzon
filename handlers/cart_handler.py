from utility.utility import *


def delete_cart(file_name, user_id):
    """
    Reverts the cart object on the selected user to empty.
    =========
    Method Arguments: 1. file name of customer list to deserialize. 2. ID of user whose cart to clear.
    """

    customer_lib = deserialize(file_name)
    customer_lib[user_id].cart = {}
    serialize(file_name, customer_lib)


def build_cart_view(customer_id):

    with sqlite3.connect("bangazon.db") as database:
            db = database.cursor()

            db.execute("""select c.CustomerId, c.FullName
                            from Order o
                            inner join Customer c on c.CustomerId = o.CustomerId
                            where o.PaymentId = Null""")
            return db.fetchall()
