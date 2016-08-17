import sqlite3
from utility.utility import *


def read_product_from_db(input_file='bangazon.db'):
    """ Reads product information from database file.
        =============
        input = name of database file from which to read.
        output = list of tuples from sqlite db/ true. The true is returned
        to denote that this particular list of tuples will have a column for
        price that the other handler database loading functions wont have.
    """

    with sqlite3.connect(input_file) as conn:
        db = conn.cursor()

        try:
            db.execute("SELECT * FROM Product")

        except sqlite3.OperationalError:
            return False

        finally:
            return db.fetchall(), True


def load_temp_product(file_name):
    """
    Loads json text file and returns it. Takes filename as argument
    ============
    file_name - a string representing the path to the file to be loaded
    """

    tempDict = read_json_file("./data/products")
    return tempDict


def generate_product_list(file_name):
    """
    loads products file and generates a menu-ized dictionary for printing and setting.
    the key will be the number the user can press to select an option, and the value is the
    txt file's product UID. Meow will use the utility get_value to print the names for each user etc.
    ============
    Method Arguments: None.
    """

    now_items = load_temp_product(file_name)
    index = 1
    item_menu = {}
    for key, value in now_items.items():
        item_menu[index] = key
        index += 1
    return item_menu
