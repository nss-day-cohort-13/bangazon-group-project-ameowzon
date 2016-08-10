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
		customer = orders_lib[obj.order_id].customer_id
		li_dict[obj.product_id]["qty"] += 1
		li_dict[obj.product_id]["customers"].append(customer)
	# calculate revenue
	for product, info in li_dict.items():
		price = products_lib[product].price
		info["revenue"] = info["qty"] * price

	row_string = "{0:<18}{1:<11}{2:<11}${3:<14}"
	total_string = "{0:<18}{1:<11}{2:<11}${3:<14}"

	########## PRINT REPORT ##########
	print(total_string.format("Products", "Orders", "Customers", "Revenue"))
	print("*" * 55)
	order_list, customer_list, revenue_list = [],[],[]
	for product, info in li_dict.items():
		product_name = products_lib[product]['name']
		order = info["qty"]
		customers = info["customers"]
		revenue = info["revenue"]

		order_list.append(order)
		customer_list.append(customer)
		revenue_list.append(revenue)

		product_name = (product_name if len(product_name) <= 17 else product_name[:14] + "...") + " "
		order = (order if len(order) <= 11 else order[:8] + "...") + " "
		customers = (customers if len(customers) <= 11 else customers[:8] + "...")
		revenue = (revenue if len(revenue) <= 14 else revenue[:11] + "...")

		print(row_string.format(product_name, order, customers, revenue))
	print("*" * 55)

	order_sum = sum(order_list)
	customer_sum = sum(customer_list)
	revenue_sum = sum(revenue_list)

	order_sum = (order_sum if len(str(order_sum)) <= 17 else order_sum[:14] + "...") + " "
	customer_sum = (customer_sum if len(str(customer_sum)) <= 11 else customer_sum[:8] + "...")
	revenue_sum = (revenue_sum if len(str(revenue_sum)) <= 14 else revenue_sum[:11] + "...")

	print(total_string.format("Totals:", order_sum, customer_sum, revenue_sum))

	########## REFACTORED PRINT STATEMENT ##########


	print("Product          Orders     Customers  Revenue        ")
	print("*" * 54)

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

	print("*" * 54)

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


