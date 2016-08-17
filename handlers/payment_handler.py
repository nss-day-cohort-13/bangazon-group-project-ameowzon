from objects.payment_object import *
import sqlite3

def generate_new_payment(name, account_number, cust_key):
	"""
	Generates a new payment object and adds it to the db

	Args-payment type name, account number, customer id payment will be associated with
	"""
	with sqlite3.connect("bangazon.db") as conn:
		c = conn.cursor()
		c.execute("""insert into PaymentMethod
			(Type, AccountNumber, CustomerId) values (?,?,?)""", (name, account_number, cust_key))
		conn.commit()

def generate_payments_menu(cust_key):
	"""
	Queries db and generates payment menu with all payment objects associated with the current customer

	Args-customer id
	"""
	with sqlite3.connect("bangazon.db") as conn:
		c = conn.cursor()
		c.execute("""select p.PaymentId, p.Type from PaymentMethod p
			inner join Customer c on p.CustomerId = c.CustomerId
			and c.CustomerId=?""", [cust_key])

		return c.fetchall(), False
