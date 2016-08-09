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
	local.setlocale(locale.LC_ALL, '')
	li_lib = deserialize("line_item.txt")
	orders_lib = deserialize("orders.txt")
	products_lib = deserialize("products.txt")
	# create dictionary with keys: product ids and values: dict of purchase info
	li_dict = {obj.product_id: {"qty": 0, "customers": set(), "revenue": 0} for uid, obj in li_lib.items()}
	# loop through all line items and populate corresponding product keys with appropriate info
	for uid, obj in li_lib.items():
		li_dict[obj.product_id]["qty"] += 1
		li_dict[obj.product_id]["customers"].append(orders_lib[obj.order_id].customer_id)
	# calculate revenue
	for product, info in li_dict.items():
		price = products_lib[product].price
		info["revenue"] = locale.currentcy((info["qty"] * price), grouping=True)
	# print report
	print("\nProduct          Orders     Customers  Revenue        ")
	print("\n*******************************************************")
	# check if product name is shorter than 15 characters
	for product, info in li_dict.items():
		if len( products_lib[product]["name"] ) - 17 < 0:
			# add appropriate amount of spaces after product name (17 - length of product name)
			product_name = "{1}{2}".format(
				products_lib[product]["name"],
				" "*(15-( len(products_lib[product]["name"]) )
			))
			# print inner columns with appropriate amount of spaces after each piece of information
			print("{1}{2}{3}{4}".format(
				product_name,
				("{1}{2}".format(info["qty"], " "*(11 - len( info["qty"] ))))
				("{1}{2}".format(len( info["customers"] ), " "*(11 - len( info["customers"] ))))
				("{1}{2}".format(info["revenue"], " "*(15 - len( info["revenue"] ))))
			))
		# if product name is longer than 17 characters, cut off everything after 17
		elif len( products_lib[product]["name"] ) - 17 >= 0:
			product_name = r_products(products_lib[product]["name"])
			# print inner columns with appropriate amount of spaces after each piece of information
			print("{1}{2}{3}{4}".format(
				product_name,
				("{1}{2}".format(info["qty"], " "*(11 - len( info["qty"] ))))
				("{1}{2}".format(len( info["customers"] ), " "*(11 - len( info["customers"] ))))
				("{1}{2}".format(info["revenue"], " "*(15 - len( info["revenue"] ))))
			))
	print("\n*******************************************************")
