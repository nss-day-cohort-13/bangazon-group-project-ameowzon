
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

import curses

try:
    class Meow():
        def __init__(self):
            # init curses
            self.screen = curses.initscr()

            self.current_user = None

        def unlogged_in_menu(self):

            # 1. log in to a user (user_menu)
            # 2. create a new user (create_new_user)
            # 3. view available products (shop_menu)
            # 4. generate report (generate_popularity_report)
            # 5. exit.
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(12, 40, "1. Log in to a user")
            self.screen.addstr(13, 40, "2. Create a new user")
            self.screen.addstr(14, 40, "3. View available products")
            self.screen.addstr(15, 40, "4. Generate report")
            self.screen.addstr(16, 40, "5. Exit")
            self.screen.refresh()

            try:
                choice = int(chr(self.screen.getch()))

                if (choice == 1):  # Log in
                    self.user_menu()

                elif (choice == 2):  # Create a new user
                    self.create_new_user()

                elif (choice == 3):  # View available products
                    self.shop_menu()

                elif (choice == 4):  # Generate report
                    self.generate_popularity_report()

                elif (choice == 5):  # Exit
                    curses.endwin()
                    exit()
                else:
                    self.unlogged_in_menu()

            except ValueError:
                self.unlogged_in_menu()

        def logged_in_menu(self):
            # print the logged-in menu options.
            # request input.
            # based on input, do:
            # 1. log out (reset_user)
            # 2. shop(shop_menu)
            # 3. payment options(payment_menu)
            # 4. product report (generate_popularity_report)
            # 5. view orders
            # 6. exit.
            pass

        def user_menu(self):
            # generate the user index. (generate_customer )
            # for each index, use get_value to print the name value.
            # request input for which user.
            pass

        def create_new_user(self):
            # request input for all the things.
            # pass all the input into the create_new_user.
            # set the current user to the UID that returns,
            # then print the logged in menu.
            pass

        def set_user(user_id):
            # set user ID to current user.
            pass

        def reset_user(self):
            # set current user to none. that's it.
            pass

        def shop_menu(self):
            # are you logged in or not?
            # if you are logged in:
            # I THINK WE SHOULD HAVE THE CART REPORT BE SEPARATE.
            # 1. for each item in your cart, get_value to print the name, per item price, quantity, total.
            # 2. total up the line item totals to print a cart total. Do we want to separate out this into a separate function?
            # 3. load_product_library and for each available product index, get_value to print the name and price.
            # 4. also add an option for completing order.
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

        def convert_to_completed(payment_uid):
            # grab user name top-level variable.
            # generate a new order uid with that user name and the UID argument.
            # for each cart item, for qty number of times, generate a line item with the product number and order number.
            # return the order number.
            pass

        def payment_options_menu(completing=False):
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

        def view_orders(self):
            # THIS IS A BITCH. DO IT LATER.
            # pass user_name top_level variable to generate_order_list.
            # for each order, print the order ID then pass it into view_line_items(?)
            # use get_value to print all the order stuff.
            pass

        def generate_popularity_report(self):
            pass

    if __name__ == '__main__':
        # Meow().print_hey()
        # print_hello()
        Meow().unlogged_in_menu()

except KeyboardInterrupt:
    curses.endwin()

    # generate_product_list("./data/products")
    # generate_customer_menu("./data/test/test_customer.txt")
    # build_temp_product()
    # load_temp_product()
