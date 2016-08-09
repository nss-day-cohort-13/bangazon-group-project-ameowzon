from utility.utility import *


def add_item_to_cart(file_name, user_id, product_id, qty):
    """
    Adds a product ID and quantity to a given user's cart. If the product ID already exists with a quantity in the cart, adds the two quantities together.
    ==========
    Method Arguments: 1. file name of customer list to deserialize. 2. ID of user whose cart to update. 3. product ID of product to add. 4. quantity of product to add.
    """

    customer_lib = deserialize(file_name)
    try:
        customer_lib[user_id].cart[product_id] += qty
    except KeyError:
        customer_lib[user_id].cart[product_id] = qty

    serialize(file_name, customer_lib)


def delete_cart(file_name, user_id):
    """
    Reverts the cart object on the selected user to empty.
    =========
    Method Arguments: 1. file name of customer list to deserialize. 2. ID of user whose cart to clear.
    """

    customer_lib = deserialize(file_name)
    customer_lib[user_id].cart = {}
    serialize(file_name, customer_lib)
