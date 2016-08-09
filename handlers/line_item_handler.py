from objects.line_item_object import *
from utility.utility import *


def generate_new_line_item(file, order_id, product_id):
	new_li = Line_Item_Object(order_id, product_id)
	new_li_id = add_to_file(file, new_li)
	return new_li_id

def build_line_item_dict():
    pass
