
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
            self.cart_id = None
            self.unlogged_in_menu()

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
            self.screen.addstr(18, 40, '')
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
                    self.quit_menu(self.unlogged_in_menu)
                else:
                    self.unlogged_in_menu()

            except ValueError:
                self.unlogged_in_menu()

        def logged_in_menu(self, name):
            # print the logged-in menu options.
            # request input.
            # based on input, do:
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(10, 40, "Welcome " + name + "!")
            self.screen.addstr(11, 40, "")
            self.screen.addstr(12, 40, '1. Log out')
            self.screen.addstr(13, 40, '2. Shop')
            self.screen.addstr(14, 40, '3. Payment options')
            self.screen.addstr(15, 40, '4. Product report')
            self.screen.addstr(16, 40, '5. Exit')
            self.screen.addstr(18, 40, '')
            self.screen.refresh()

            try:
                choice = int(chr(self.screen.getch()))

                if choice == 1:
                    self.reset_user()
                    self.unlogged_in_menu()

                elif choice == 2:
                    self.shop_menu()

                elif choice == 3:
                    self.payment_options_menu()

                elif choice == 4:
                    self.generate_popularity_report()

                elif choice == 5:
                    self.quit_menu(self.logged_in_menu)

            except ValueError:
                self.logged_in_menu()

        def quit_menu(self, back_to_menu):
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(12, 40, 'Are you sure you want to exit? [ y / n ]')
            self.screen.addstr(14, 40, '')
            self.screen.refresh()

            try:
                choice = chr(self.screen.getch())

                if choice.lower() == 'y':
                    curses.endwin()
                    quit()
                else:
                    if self.current_user is None:
                        self.unlogged_in_menu()
                    else:
                        back_to_menu()

            except ValueError:
                back_to_menu()

        def user_menu(self):
            # generate the customer menu.
            # for each customer item, use get_value to print the name value.
            # request input for which user.
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(11, 40, "'q to quit, b to go back.")
            user_list = print_menu(generate_customer_menu, self.screen, 12)
            self.screen.refresh()

            choice = (chr(self.screen.getch()))
            if choice == "b":
                self.unlogged_in_menu()
            elif choice == "q":
                self.quit_menu(self.user_menu)
            else:
                try:
                    choice = int(choice)
                except ValueError:
                    self.user_menu()
                except TypeError:
                    self.user_menu()
                finally:
                    try:
                        user_uid = set_thing(user_list, choice)
                        name = get_customer_name(user_uid)
                    except TypeError:
                        self.user_menu()
                    # except IndexError:
                    #     self.user_menu()
                    # except ValueError:
                    #     self.user_menu()
                    finally:
                        self.set_user(user_uid)
                        self.logged_in_menu(name)

        def create_new_user(self):
            # request input for all the things.
            # pass all the input into the create_new_user.
            # set the current user to the UID that returns,
            # then print the logged in menu.
            name = get_param('What is your name?', self.screen)
            address = get_param('What is your street address?', self.screen)
            city = get_param('What city do you live in?', self.screen)
            state = get_param('What state do you live in?', self.screen)
            zipcode = get_param('What is your zipcode?', self.screen)
            phone = get_param('What is your phone number?', self.screen)

            try:
                new_uid = generate_new_customer('data/customers.txt', name, address, city, state, zipcode, phone)
                self.set_user(new_uid)
                self.logged_in_menu()
            except:
                self.unlogged_in_menu()

        def set_user(self, user_id):
            # set user ID to current user.
            self.current_user = user_id

        def reset_user(self):
            # set current user to none. that's it.
            self.current_user = None

        def shop_menu(self):

            """
            This function prints a list of products and prices from products.txt, saved as a index-uid dictionary in a scoped product_menu variable.  Then it requests next_step input from the user. If the user is not logged in, the only subsequent options are to go back or exit. If the user is logged in, they have the option of adding an item to their cart (via product_menu) or completing their order via payment_options_menu.
            ==========
            Method Arguments: none.
            """
            # load_product_library and for each available product index, get_value to print the name and price.
            self.screen.clear()
            self.screen.border(0)

            row = 3
            product_list = print_menu(read_product_from_db, self.screen, row)
            row += len(product_list)

            # are you logged in or not?
            row += 2
            if self.current_user is not None:
                # view your cart or note that it's empty.
                self.view_cart()
                self.screen.addstr(row, 22, "Press the number of the item you'd like to add to your cart.")
                row += 1
                self.screen.addstr(row, 22, "Or press'c' to check out, 'b' to go back, 'x' to exit.")
                row += 1

                try:
                    next_step = chr(self.screen.getch())
                    row += 1
                    if next_step == "x":  # Exit.
                        self.quit_menu(self.shop_menu)

                    elif next_step == "b":  # Go back.
                        self.logged_in_menu()

                    elif next_step == "c":  # Check Out.
                        self.payment_options_menu(completing=True)

                    else:
                        self.screen.addstr(row, 40, next_step)
                        row += 1
                        try:  # Add a product to your cart.
                            next_step = int(next_step)
                        except ValueError:
                            self.shop_menu()
                        finally:
                            row += 2
                            if next_step >= 0 and next_step < len(product_list):
                                prod_id = set_thing(product_list, next_step)
                                self.add_to_cart_menu(prod_id)
                            else:
                                # print("command not recognized.")
                                self.screen.addstr(row, 40, "Command not recognized.")
                                self.shop_menu()

                except ValueError:
                    self.unlogged_in_menu()

            else:
                # if you're not logged in you can view products, but you can't do anything with a cart.
                self.screen.addstr(row, 40, "You are not logged in.")
                self.screen.addstr(row + 1, 12, "Press 'b' to go back and choose a login option, or x to exit.")

                next_step = chr(self.screen.getch())

                if next_step == "b":
                    self.unlogged_in_menu()
                elif next_step == "x":
                    self.quit_menu(self.shop_menu)
                else:
                    self.screen.addstr(17, 40, "Command_not_recognized.")
                    # print("command_not_recognized.")

        def add_to_cart_menu(self, prod_ID):
            """
            Receives a unique id for a product to add to the current user's 'cart' property. To separate concerns from shop_menu, this function requests the quantity to add, and adds the item to the cart.
            ==========
            Arguments: product id
            """
            self.screen.clear()
            self.screen.border(0)
            row = 4
            product_name = get_product_name(prod_id)
            self.screen.addstr(row, 22, "how many " + product_name + "'s would you like to add?")
            # print("how many" + prod_id["name"] + "s would you like to add?")
            row += 1
            self.screen.addstr(row, 22, "'b' to go back, 'x' to exit.")
            # print("'b' to go back, 'x' to exit.")
            # quantity = input(">> ")
            quantity = chr(self.screen.getch())

            if quantity == "b":  # go back.
                self.shop_menu()
            elif quantity == "x":  # exit.
                self.quit_menu(self.shop_menu)
            else:
                try:  # add a qty of items to cart property on the current user object.
                    quantity = int(quantity)
                except ValueError:
                    # print("command not recognized.")
                    self.add_to_cart_menu(prod_ID)
                finally:
                    # add (quantity) line items to open order (self.cart_id)
                    for i in range(quantity + 1):
                        generate_new_line_item(self.cart_id, prod_id)
                    row += 3
                    self.screen.addstr(row, 40, str(quantity) + " " + product_name + " added to cart.")
                    row += 3
                    self.screen.addstr(row, 40, "Press 'any key' to return to shopping menu.")

                    quantity = chr(self.screen.getch())

                    if (quantity):
                        self.shop_menu()

                    # print(quantity + item_to_add["name"] + " added to cart.")
                    # self.shop_menu()

        def view_cart(self):
            """
            Displays the cart of the currently logged in user. Handles what to say if the user does not have a cart or if their cart is empty.
            ========
            Method Arguments: None
            """

            # check if user has a cart.
            self.cart_id = check_if_cart_exists(self.current_user)
            if self.cart_id is None:
                # if they don't have a cart, create one and print "your cart is empty, start shopping"
                new_order(self.current_user)
                self.screen.addstr(12, 40, "Your cart is empty. Start shopping!")
            else:
                cart_to_print = build_cart_view(self.cart_id)
                # if they have a cart, check if cart is not empty.
                if len(cart_to_print) == 0:
                    self.screen.addstr(12, 40, "Your cart is empty. Start shopping!")
                else:
                    # if it's not empty, print it.
                    # format for columns
                    row_string = "{0:<18}{1:<11}${2:<14}"
                    total_string = "{0:<29}${1:<14}"
                    heading_string = "{0:<29}{1:<14}"
                    total_list = []
                    row = 18
                    self.screen.addstr(row, 40, heading_string.format("Your cart:", "Totals:"))
                    row += 1
                    self.screen.addstr(row, 40, "*" * 44)
                    row += 1
                    # loop over cart items and calculate total (grab price from 'products.txt')
                    for index, item in cart_to_print:
                        # append total to list of totals (for amount due calculation)
                        total_list.append(item[2])
                        # limit product name
                        product_name = (item[0] if len(item[0]) <= 17 else item[0][:14] + "...") + " "
                        # print
                        self.screen.addstr(row, 40, row_string.format(product_name, item[1], item[2]))
                        row += 1
                    self.screen.addstr(row, 40, "*" * 44)
                    row += 1
                    # self.screen.addstr out total amount due
                    self.screen.addstr(row, 40, total_string.format("Order total:", sum(total_list)))

        def convert_to_completed(self, payment_uid):
            # add payment id to customers open order, direct to logged-in menu
            add_payment_to_order(self.current_user, payment_uid)
            self.logged_in_menu()

        def payment_options_menu(self, completing=False):
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(3, 20, "Your payment types:")

            how_far_down = 5
            payment_list = print_menu(generate_payments_menu, self.screen, how_far_down, cid=self.current_user)
            how_far_down += len(payment_list)

            # for each payment id in payment_list, use get_value to print the name or something.
            if len(payment_list) == 0:
                self.screen.addstr(how_far_down, 40, "No payment types yet!")
                how_far_down += 1
            else:
                pass

            self.screen.addstr(how_far_down, 40, '')
            how_far_down += 1
            self.screen.refresh()

            if completing is False:
                self.screen.addstr(how_far_down, 22, "n for new payment. b to go back. x to exit.")
                next_step = chr(self.screen.getch())
                if next_step == "n":
                    self.new_payment()
                    self.payment_options_menu(completing=completing)
                elif next_step == "b":
                    self.logged_in_menu()
                elif next_step == "x":
                    self.quit_menu(self.payment_options_menu)
                else:
                    self.payment_options_menu()
            elif completing is True:
                self.screen.addstr(how_far_down, 40, "Press the number of the payment to use for this order.")
                how_far_down += 1
                self.screen.addstr(how_far_down, 40, "n to make a new payment. b to go back. x to exit.")
                how_far_down += 1
                next_step = chr(self.screen.getch())
                if next_step == "n":
                    self.payment_options_menu(completing=False)
                elif next_step == "b":
                    self.shop_menu()
                elif next_step == "x":
                    self.quit_menu(self.shop_menu)
                else:
                    try:
                        next_step = int(next_step)
                    except ValueError:
                        self.payment_options_menu(completing=True)
                    finally:
                        if next_step >= 0 and next_step < len(payment_list):
                            payment_uid = set_thing(payment_list, next_step)
                            self.convert_to_completed(payment_uid)
                        else:
                            self.payment_options_menu(True)

        def new_payment(self):
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(12, 40, 'Add a new account:')
            self.screen.refresh()
            account_num = get_param("enter the account number.", self.screen)
            account_name = get_param("enter a nickname for this account.", self.screen)
            generate_new_payment(account_name, account_num, self.current_user)

        def generate_popularity_report(self):
            """
            Generates a report that lists how many times a product was bought, by how many customers,
            and how much money each has brought in

            Args-None
            """
            self.screen.clear()
            self.screen.border(0)
            # initial method setup
            li_lib = deserialize("data/line_items.txt")
            orders_lib = deserialize("data/orders.txt")
            products_lib = deserialize("data/products.txt")

            ########## BUILD POPULARITY DICT ##########
            # create dictionary with keys: product ids and values: dict of purchase info
            total_customers = set()
            li_dict = {obj.product_id: {"qty": 0, "customers": set(), "revenue": 0} for uid, obj in li_lib.items()}
            # loop through all line items and populate corresponding product keys with appropriate info
            for uid, obj in li_lib.items():
                customer = orders_lib[obj.order_id].customer_id
                li_dict[obj.product_id]["qty"] += 1
                li_dict[obj.product_id]["customers"].add(customer)
                total_customers.add(customer)
            # self.screen.addstr(1, 20, str(li_dict))
            # calculate revenue
            for product, info in li_dict.items():
                price = products_lib[product]["price"]
                info["revenue"] = info["qty"] * price

            heading_string = "{0:<18}{1:<11}{2:<11}{3:<15}"
            row_string = "{0:<18}{1:<11}{2:<11}${3:<14}"
            total_string = "{0:<18}{1:<11}{2:<11}${3:<14}"

            ########## PRINT REPORT ##########
            row = 5
            # self.screen.addstr(row, 40, str(li_lib))
            row += 1
            # print(total_string.format("Products", "Orders", "Customers", "Revenue"))
            self.screen.addstr(row, 40, heading_string.format("Products", "Orders", "Customers", "Revenue"))
            row += 1
            self.screen.addstr(row, 40, "*" * 55)
            row += 1
            # print("*" * 55)
            order_list, customer_list, revenue_list = [], [], []
            for product, info in li_dict.items():
                # set product names
                product_name = products_lib[product]['name']
                order = info["qty"]
                customers = info["customers"]
                revenue = info["revenue"]

                # add values to lists (to be used in totals calculation)
                order_list.append(order)
                customer_list.append(customer)
                revenue_list.append(revenue)

                # limit display names/values
                product_name = (product_name if len(product_name) <= 17 else product_name[:14] + "...") + " "
                order = (str(order) if len(str(order)) <= 11 else str(order[:8]) + "...") + " "
                customers = (len(customers) if len(customers) <= 11 else len(customers)[:8] + "...")
                revenue = (str(revenue) if len(str(revenue)) <= 14 else str(revenue[:11]) + "...")

                # print product info
                self.screen.addstr(row, 40, row_string.format(product_name, order, customers, revenue))
                # print(row_string.format(product_name, order, customers, revenue))
                row += 1
            self.screen.addstr(row, 40, "*" * 55)
            # print("*" * 55)

            # calculate totals
            order_sum = sum(order_list)
            customer_sum = len(total_customers)
            revenue_sum = sum(revenue_list)

            # limit totals display
            order_sum = (str(order_sum) if len(str(order_sum)) <= 17 else str(order_sum[:14]) + "...") + " "
            customer_sum = (str(customer_sum) if len(str(customer_sum)) <= 11 else str(customer_sum[:8]) + "...")
            revenue_sum = (str(revenue_sum) if len(str(revenue_sum)) <= 14 else str(revenue_sum[:11]) + "...")

            # print totals
            row += 1
            self.screen.addstr(row, 40, total_string.format("Totals:", order_sum, customer_sum, revenue_sum))
            # print(total_string.format("Totals:", order_sum, customer_sum, revenue_sum))
            row += 1
            self.screen.addstr(row, 40, "press any key to continue")
            choice = chr(self.screen.getch())
            if self.current_user is not None:
                self.logged_in_menu()
            else:
                self.unlogged_in_menu()

    if __name__ == '__main__':
        # Meow().print_hey()
        # print_hello()
        # Meow().unlogged_in_menu()
        Meow()

except KeyboardInterrupt:
    curses.endwin()
