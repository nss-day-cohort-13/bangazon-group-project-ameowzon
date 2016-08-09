from objects.payment_object import *
from utility.utility import *

def generate_new_payment(file, name, account_number, cust_key):
    new_payment = Payment_Object(name, account_number, cust_key)
    add_to_file(file, new_payment)

def generate_payments_menu(file):
	lib = deserialize(file)
	counter = 1
	payments_menu = dict()
	for uid, obj in lib.items():
		payments_menu[counter] = uid
		counter += 1
	return payments_menu

