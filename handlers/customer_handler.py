from objects.customer_object import *
from utility.utility import *
import sqlite3


def generate_new_customer(file_name="", name="", address="", city="", state="", zipcode="", phone=""):
    """
    Uses instantiate_new_customer and add_to_file (in utility module) to generate a customer item based on their inputs, deserialize customers.txt file, add the new customer to the file, and return a newly generated customer UID(generated in add_to_file).
    ===========
    Method Arguments: strings. 1. file_name of txt file to add to, 2. name, 3. address, 4. city, 5. state, 6. zipcode, 7. phone. Note that these are keyed arguments so can be passed in any order if specified with the appropriate key.
    """
    customer_to_add = instantiate_customer_object(name, address, city, state, zipcode, phone)
    customer_id = add_to_file(file_name, customer_to_add)
    return customer_id


def instantiate_customer_object(name, address, city, state, zipcode, phone):
    """
    Runs inside generate_new_customer to instantiate a new customer object with name, address, city, state, zipcode, and phone properties. Returns a Customer_Object.
    =========
    Method Arguments: strings. 1. name, 2. address, 3. city, 4. state, 5. zipcode, 6. phone.
    """
    new_customer = Customer_Object(name, address, city, state, zipcode, phone)
    return new_customer


def generate_customer_menu():
    """
    deserializes customers.txt and generates a menu-ized dictionary for printing and setting. the key will be the number the user can press to select an option, and the value is the txt file's customer UID. Meow will use the utility get_value to print the names for each user etc.
    ============
    Method Arguments: None.
    """
    # now_customers = deserialize(file_name)
    # index = 1
    # customer_menu = {}
    # for key, value in now_customers.items():
    #     customer_menu[index] = key
    #     index += 1

    # return customer_menu

    with sqlite3.connect("bangazon.db") as database:
        db = database.cursor()

        db.execute("""select c.CustomerId, c.FullName
                        from Customer as c""")
        print(db.fetchall())
