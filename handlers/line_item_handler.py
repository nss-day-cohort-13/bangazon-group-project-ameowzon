from objects.line_item_object import *
from utility.utility import *


def generate_new_line_item(file, order_id, product_id):
    """
    Creates a new line item object

    Args-file name, order ID that line item is associated with, product ID that line item associated with
    """
    new_li = Line_Item_Object(order_id, product_id)
    new_li_id = add_to_file(file, new_li)
    return new_li_id

# def generate_popularity_report():
#     """
#     Generates a report that lists how many times a product was bought, by how many customers,
#     and how much money each has brought in

#     Args-None
#     """
#     # initial method setup
#     li_lib = deserialize("line_item.txt")
#     orders_lib = deserialize("orders.txt")
#     products_lib = deserialize("products.txt")

#     ########## BUILD POPULARITY DICT ##########
#     # create dictionary with keys: product ids and values: dict of purchase info
#     li_dict = {obj.product_id: {"qty": 0, "customers": set(), "revenue": 0} for uid, obj in li_lib.items()}
#     # loop through all line items and populate corresponding product keys with appropriate info
#     for uid, obj in li_lib.items():
#         customer = orders_lib[obj.order_id].customer_id
#         li_dict[obj.product_id]["qty"] += 1
#         li_dict[obj.product_id]["customers"].append(customer)
#     # calculate revenue
#     for product, info in li_dict.items():
#         price = products_lib[product].price
#         info["revenue"] = info["qty"] * price

#     row_string = "{0:<18}{1:<11}{2:<11}${3:<14}"
#     total_string = "{0:<18}{1:<11}{2:<11}${3:<14}"

#     ########## PRINT REPORT ##########
#     print(total_string.format("Products", "Orders", "Customers", "Revenue"))
#     print("*" * 55)
#     order_list, customer_list, revenue_list = [],[],[]
#     for product, info in li_dict.items():
#         # set product names
#         product_name = products_lib[product]['name']
#         order = info["qty"]
#         customers = info["customers"]
#         revenue = info["revenue"]

#         # add values to lists (to be used in totals calculation)
#         order_list.append(order)
#         customer_list.append(customer)
#         revenue_list.append(revenue)

#         # limit display names/values
#         product_name = (product_name if len(product_name) <= 17 else product_name[:14] + "...") + " "
#         order = (order if len(order) <= 11 else order[:8] + "...") + " "
#         customers = (customers if len(customers) <= 11 else customers[:8] + "...")
#         revenue = (revenue if len(revenue) <= 14 else revenue[:11] + "...")

#         # print product info
#         print(row_string.format(product_name, order, customers, revenue))
#     print("*" * 55)

#     # calculate totals
#     order_sum = sum(order_list)
#     customer_sum = sum(customer_list)
#     revenue_sum = sum(revenue_list)

#     # limit totals display
#     order_sum = (order_sum if len(str(order_sum)) <= 17 else order_sum[:14] + "...") + " "
#     customer_sum = (customer_sum if len(str(customer_sum)) <= 11 else customer_sum[:8] + "...")
#     revenue_sum = (revenue_sum if len(str(revenue_sum)) <= 14 else revenue_sum[:11] + "...")

#     # print totals
#     print(total_string.format("Totals:", order_sum, customer_sum, revenue_sum))
