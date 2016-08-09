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

def generate_popularity_report(file):
	"""
	Generates a report that lists how many times a product was bought, by how many customers,
	and how much money each has brought in

	Args-file name
	"""
	lib = deserialize(file)
	li_dict = {obj.product_id: 0 for uid, obj in lib.items()}
