import sys
sys.path.append("./handlers")
from customer_handler import *
from line_item_handler import *
from order_handler import *
from payment_handler import *
from product_handler import *
# sys.path.append("./objects")
# from customer_object import *
# from line_item_object import *
# from order_object import *
# from payment_object import *
# from product_object import *


class Meow():
    def print_hey():
        print("Hey")
        pass

    def set_current_user():
        pass

    def select_payment():
        pass

    def add_to_cart():
        pass

    def retrieve_cart():
        pass

    def calculate_total():
        pass

    def convert_to_completed():
        pass

if __name__ == '__main__':
    Meow().print_hey()
