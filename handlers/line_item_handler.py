import locale
import reprlib
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

def generate_popularity_report():
	"""
	Generates a report that lists how many times a product was bought, by how many customers,
	and how much money each has brought in

	Args-None
	"""
	r_products = reprlib.Repr()
	r_products.maxstring = 17
	r_orders_cust = reprlib.Repr()
	r_orders_cust.maxstring = 11
	r_revenue = reprlib.Repr()
	r_revenue.maxstring = 15
	local.setlocale(locale.LC_ALL, '')
	li_lib = deserialize("line_item.txt")
	orders_lib = deserialize("orders.txt")
	products_lib = deserialize("products.txt")
	li_dict = {obj.product_id: {"qty": 0, "customers": set(), "revenue": 0} for uid, obj in li_lib.items()}
	for uid, obj in li_lib.items():
		li_dict[obj.product_id]["qty"] += 1
		li_dict[obj.product_id]["customers"].append(orders_lib[obj.order_id].customer_id)
	for product, info in li_dict.items():
		price = products_lib[product].price
		info["revenue"] = locale.currentcy((info["qty"] * price), grouping=True)
	print("\nProduct          Orders     Customers  Revenue        ")
	print("\n*******************************************************")

	for product, info in li_dict.items():
		if len(products_lib[product]["name"]) - 15 < 0:
			product_name = "{1}{2}".format(
				products_lib[product]["name"],
				" "*(15-(len(products_lib[product]["name"]))
			))
