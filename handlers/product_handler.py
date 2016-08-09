from objects.product_object import *
from utility.utility import *


def build_temp_product():
    '''Reads json text file and deserializes it into a dictionary. Returns
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


def load_temp_product():

    tempDict = read_json_file("./data/products")
    return tempDict
