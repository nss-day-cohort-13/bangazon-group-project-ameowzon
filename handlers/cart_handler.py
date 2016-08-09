from utility.utility import *


def add_item_to_cart(file_name, user_id, product_id, qty):

    customer_lib = deserialize(file_name)
    try:
        customer_lib[user_id].cart[product_id] += qty
    except KeyError:
        customer_lib[user_id].cart[product_id] = qty

    serialize(file_name, customer_lib)


def delete_cart(file_name, user_id):

    customer_lib = deserialize(file_name)
    customer_lib[user_id].cart = {}
    serialize(file_name, customer_lib)
