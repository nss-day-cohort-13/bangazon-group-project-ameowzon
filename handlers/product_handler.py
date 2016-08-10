from utility.utility import *


def build_temp_product():
    '''
    Reads json text file and deserializes it into a dictionary. Returns
    a uuid.
    '''

    tempDict = dict()
    products = read_json_file("./data/test/products.json")
    products = products["cats"]

    for entry in products:
        uid = generate_uid()
        tempDict[uid] = {"name": entry['name'], "price": entry['price']}

    write_json_file(tempDict, "./data/products")
    return tempDict


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
