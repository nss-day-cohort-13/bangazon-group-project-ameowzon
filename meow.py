import sys
sys.path.append("./handlers")
sys.path.append("./objects")
from customer_handler import *
from line_item_handler import *
from order_handler import *
from payment_handler import *
from product_handler import *
from customer_object import *
from line_item_object import *
from order_object import *
from payment_object import *
from product_object import *


class Meow():
    print("Hey")
    pass

if __name__ == '__main__':
    Meow()
