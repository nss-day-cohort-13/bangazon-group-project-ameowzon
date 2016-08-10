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
	# initial method setup
	r_products = reprlib.Repr()
	r_products.maxstring = 17
	r_order_cust = reprlib.Repr()
	r_order_cust.maxstring = 11
	r_revenue = reprlib.Repr()
	r_revenue.maxstring = 15
	local.setlocale(locale.LC_ALL, '')
	li_lib = deserialize("line_item.txt")
	orders_lib = deserialize("orders.txt")
	products_lib = deserialize("products.txt")

	########## BUILD POPULARITY DICT ##########
	# create dictionary with keys: product ids and values: dict of purchase info
	li_dict = {obj.product_id: {"qty": 0, "customers": set(), "revenue": 0} for uid, obj in li_lib.items()}
	# loop through all line items and populate corresponding product keys with appropriate info
	for uid, obj in li_lib.items():
		li_dict[obj.product_id]["qty"] += 1
		li_dict[obj.product_id]["customers"].append(orders_lib[obj.order_id].customer_id)
	# calculate revenue
	for product, info in li_dict.items():
		price = products_lib[product].price
		info["revenue"] = info["qty"] * price

	########## PRINT REPORT ##########
	print("Product          Orders     Customers  Revenue        ")
	print("*******************************************************")
	# check if product name is shorter than 15 characters
	for product, info in li_dict.items():
		if len( products_lib[product]["name"] ) - 17 < 0:
			# add appropriate amount of spaces after product name (17 - length of product name)
			product_name = "{1}{2}".format(
				products_lib[product]["name"],
				" "*(17-( len(products_lib[product]["name"]) )
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
	print("*******************************************************")

	########## REFACTORED PRINT STATEMENT ##########

	product_name = products_lib[product]['name']
	order = info["qty"]
	customers = info["customers"]
	revenue = info["revenue"]
	order_list, customer_list, revenue_list = [],[],[]

	print("Product          Orders     Customers  Revenue        ")
	print("*******************************************************")

	for product, info in li_dict.items():
		# check product name length
		if len(product_name) - 17 < 0:
			product_name = "{1}{2}".format(
				product_name,
				" " * (17 - len(product_name))
			)
		elif len(product_name) - 17 >= 0:
			product_name = r_products(product_name)

		# check order string length
		if len(str(order)) - 11 < 0:
			order = "{1}{2}".format(
				order,
				" " * (11 - len(str(order)))
			)
		elif len(order) - 11 >= 0:
			order = r_order_cust(order)

		# check customer string length
		if len(str(customer)) - 11 < 0:
			customer = "{1}{2}".format(
				customer,
				" " * (11 - len(str(customer)))
			)
		elif len(customer) - 11 >= 0:
			customer = r_order_cust(customer)

		# check revenue string length
		if len(str(locale.currency(sum(revenue), grouping=True))) - 15 < 0:
			revenue = "{1}{2}".format(
				revenue,
				" " * (15 - len(str(revenue)))
			)
		elif len(str(locale.currency(sum(revenue), grouping=True))) - 15 >= 0:
			revenue = r_revenue(revenue)

		# add info to respective lists (to be used for totals)
		order_list.append(order)
		customer_list.append(customer)
		revenue_list.append(revenue)

		# print data
		print("{1}{2}{3}{4}".format(product_name, order, customer, locale.currency(revenue, grouping=True)))

	print("*******************************************************")

	########## CALCULATE TOTALS ##########

	# check order sum length
	if len(str(sum(order_list))) - 11 < 0:
		order_sum = "{1}{2}".format(
			sum(order_list),
			" " * (11 - len(str(order)))
		)
	elif len(str(sum(order_list))) - 11 >= 0:
		order_sum = r_order_cust(sum(order_list))

	# check customer sum length
	if len(str(customer)) - 11 < 0:
		customer = "{1}{2}".format(
			sum(customer_list),
			" " * (11 - len(str(customer)))
		)
	elif len(str(sum(customer_list))) - 11 >= 0:
		customer_sum = r_order_cust(sum(customer_list))

	# check revenue sum length
	if len(str(locale.currency(sum(revenue), grouping=True))) - 15 < 0:
		revenue_list = "{1}{2}".format(
			sum(revenue_list),
			" " * (15 - len(str(revenue)))
		)
	elif len(str(locale.currency(sum(revenue), grouping=True))) - 15 >= 0:
		revenue_sum = r_revenue(sum(revenue_list))

	# print totals
	print("{1}{2}{3}{4}".format(
		"                 ",
		order_sum,
		customer_sum,
		locale.currency(revenue_sum, grouping=True)))


