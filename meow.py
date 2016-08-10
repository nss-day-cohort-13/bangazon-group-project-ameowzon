
from handlers.customer_handler import *
from handlers.line_item_handler import *
from handlers.order_handler import *
from handlers.payment_handler import *
from handlers.product_handler import *
from handlers.cart_handler import *

from objects.customer_object import *
from objects.line_item_object import *
from objects.order_object import *
from objects.payment_object import *
from objects.product_object import *


class Meow():

    self.current_user = None

    def unlogged_in_menu(self):
        # print the unlogged-in menu options.
        # request input
        # based on input, do:
        # 1. log in to a user (user_menu)
        # 2. create a new user (create_new_user)
        # 3. view available products (shop_menu)
        # 4. generate report (generate_popularity_report)
        # 5. exit.
        pass

    def logged_in_menu(self):
        # print the logged-in menu options.
        # request input.
        # based on input, do:
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(12, 40, '1. Log out')
        self.screen.addstr(13, 40, '2. Shop')
        self.screen.addstr(14, 40, '3. Payment options')
        self.screen.addstr(15, 40, '4. Product report')
        self.screen.addstr(16, 40, '5. Exit')
        self.screen.refresh()

        try:
            choice = int(chr(self.screen.getch()))

            if choice == 1:
                self.reset_user()

            elif choice == 2:
                self.shop_menu()

            elif choice == 3:
                self.payment_options_menu()

            elif choice == 4:
                self.generate_popularity_report()

            elif choice == 5:
                self.quit_menu()

        except ValueError:
            self.logged_in_menu()

    def quit_menu(self):
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(12, 40, 'Are you sure you want to exit? [ y / n ]')
        self.screen.refresh()

        try:
            choice = chr(self.screen.getch())

            if choice.lower() == 'y':
                quit()
            else:
                self.logged_in_menu()

        except ValueError:
            self.logged_in_menu()


    def user_menu(self):
        # generate the customer menu.
        # for each customer item, use get_value to print the name value.
        # request input for which user.
        pass

    def create_new_user(self):
        # request input for all the things.
        # pass all the input into the create_new_user.
        # set the current user to the UID that returns,
        # then print the logged in menu.
        pass

    def set_user(self, user_id):
        # set user ID to current user.
        pass

    def reset_user(self):
        # set current user to none. that's it.
        current_user = None

    def shop_menu(self):
        # are you logged in or not?
        # if you are logged in:
        # 1. load view_cart so all the math gets done.
        # 2. load_product_library and for each available product index, get_value to print the name and price.
        # 3. also add an option for completing order.
        # 4. request input for an item to add, or whether you'd ike to complete your order.
        # if you'd like to add an item:
        # 5. request input for the quantity to add.
        # 6. pass the name and quantity to add_item_to_cart.
        # if you'd like to complete your order:
        # run payment_options_menu and pass completing=True so it asks the appropriate questions.
        # if you are not logged in:
        # load_product_library and for each available product index, get_value to print the name and price.
        # request input to go back or exit.
        pass

    def view_cart(self):
        # 1. for each item in your cart, get_value to print the name, per item price, quantity, total.
        # 2. total up the line item totals to print a cart total. Do we want to separate out this into a separate function?
        pass

    def convert_to_completed(self, payment_uid):
        # grab user name top-level variable.
        # generate a new order uid with that user name and the UID argument.
        # for each cart item, for qty number of times, generate a line item with the product number and order number.
        # return the order number.
        pass

    def payment_options_menu(self, completing=False):
        # pass user name top-level variable to generate_payment_list.
        # for each payment id in payment_list, use get_value to print the name or something.
        # if completing == false
        # request input to either add a new payment or go back.
        # if they'd like to add a new payment, request input for all the data,
        # then pass it to generate_new_payment and restart the function.
        # if completing == true
        # request input to either add a new payment or select a current payment.
        # if they'd like to add a new payment, request input for all the data,
        # then pass it to generate_new_payment and restart the function to print the updated list of payments.
        # if they select a current payment:
        # pass the payment uid to convert to completed.
        # print the order number, and print the top level logged-in menu.
        pass

    def generate_popularity_report(self):
        pass

if __name__ == '__main__':
    # generate_product_list("./data/products")
    generate_customer_menu("./data/test/test_customer.txt")
    # build_temp_product()
    # load_temp_product()

    # objects are classes
