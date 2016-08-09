from objects.payment_object import *
from utility.utility import *

def generate_new_payment(file, name, account_number, cust_key):
	"""
	Generates a new payment object and adds it to the passed in file name

	Args-file name, payment type name, account number, customer payment will be associated with
	"""
	new_payment = Payment_Object(name, account_number, cust_key)
	payment_id = add_to_file(file, new_payment)
	return payment_id

def generate_payments_menu(file, cust_key):
	"""
	Generates payment menu with all payment objects associated with the current customer

	Args-file name, customer
	"""
	lib = deserialize(file)
	counter = 1
	payments_menu = dict()
	for uid, obj in lib.items():
		if obj.customer == cust_key:
			payments_menu[counter] = uid
			counter += 1
	return payments_menu

