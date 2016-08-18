

from handlers.customer_handler import *
from handlers.line_item_handler import *
from handlers.order_handler import *
from handlers.payment_handler import *
from handlers.product_handler import *
from handlers.cart_handler import *
from handlers.admin_handler import *

import curses

try:
    class Meow():
        def __init__(self):
            # init curses
            self.screen = curses.initscr()
            self.current_user = None
            self.user_name = ""
            self.cart_id = None

        def unlogged_in_menu(self):
            """
            Prints top-level menu options for a unlogged-in user, and requests next-step input. Based on the input, continues to the next menu.
            Menu options: 1. log in to an existing user (new user menu). 2. create a new user (new user menu). 3. view available products (shop menu). 4. view popularity report. 5. exit.
            ========
            Method Arguments: None
            """
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(12, 40, "1. Log in to a user")
            self.screen.addstr(13, 40, "2. Create a new user")
            self.screen.addstr(14, 40, "3. View available products")
            self.screen.addstr(15, 40, "4. Generate report")
            self.screen.addstr(16, 40, "5. Exit")
            self.screen.addstr(18, 40, "6. Admin login")
            self.screen.addstr(20, 40, '')
            self.screen.refresh()

            try:
                choice = int(chr(self.screen.getch()))
            except ValueError:
                self.unlogged_in_menu()
            finally:
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

                elif (choice == 6):
                    self.verify_admin_menu()

                else:
                    self.unlogged_in_menu()

        def logged_in_menu(self):
            """
            Prints top-level menu options for a logged-in user, and requests next-step input. Based on the input, continues to the next menu.
            Menu options: 1. log out and return to unlogged in menu. 2. shop (go to shop menu). 3. view payment options menu. 4. view popularity report. 5. exit.
            ========
            Method Arguments: None
            """
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(10, 40, "Welcome " + self.user_name + "!")
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
            except ValueError:
                self.logged_in_menu()
            finally:
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

                else:
                    self.logged_in_menu()

        def quit_menu(self, back_to_menu):
            """
            This function is called if the user enters 'quit' input in any other menu. Asks the user if they really want to quit, and based on their final input, either quits or goes back to the previous menu.
            ========
            Method argument: the name of the function to go back to if the user changes their mind about quitting.
            """
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
            """
            Prints the list of users currently created, and requests input from the user for whether they'd like to choose one of the options to log into, or go back.
            ========
            Method Arguments: None
            """
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
                        self.current_user = set_thing(user_list, choice)
                        self.user_name = get_customer_name(self.current_user)
                    except TypeError:
                        self.user_menu()
                    except IndexError:
                        self.user_menu()
                    finally:
                        self.logged_in_menu()

        def create_new_user(self):
            """
            Requests input for each of the parameters required to create a new user (name, address, city, state, zip, and phone). Passes the information into generate_new_customer and receives the UID back, which it sets to the current user. Sets the user_name top-level variable (which is printed as a greeting in the logged in menu) and directs to the logged in menu.
            ========
            Method Arguments: none
            """
            name = get_param('What is your name?', self.screen)
            address = get_param('What is your street address?', self.screen)
            city = get_param('What city do you live in?', self.screen)
            state = get_param('What state do you live in?', self.screen)
            zipcode = get_param('What is your zipcode?', self.screen)
            phone = get_param('What is your phone number?', self.screen)

            try:
                self.current_user = generate_new_customer(name, address, city, state, zipcode, phone)
                self.user_name = name
                self.logged_in_menu()
            except:
                self.unlogged_in_menu()

        def reset_user(self):
            """
            Sets current user to none as part of logging out.
            ========
            Method Arguments: None
            """
            self.current_user = None
            self.user_name = ""
            self.cart_id = None

        def shop_menu(self):

            """
            Prints a list of products and prices from the products table in bangazon.db. Then requests next_step input from the user. If the user is not logged in, the only subsequent options are to go back or exit. If the user is logged in, their cart prints via view_cart, and they have the option of adding an item to their cart (via product_menu) or completing their order via payment_options_menu.
            ==========
            Method Arguments: none.
            """
            self.screen.clear()
            self.screen.border(0)

            row = 3
            # load_product_library and for each available product index, get_value to print the name and price.
            product_list = print_menu(read_product_from_db, self.screen, row)
            row += len(product_list)

            # are you logged in or not?
            row += 2
            if self.current_user is not None:
                # view your cart or note that it's empty.
                self.screen.addstr(row, 22, "Press the number of the item you'd like to add to your cart.")
                row += 1
                self.screen.addstr(row, 22, "Or press'c' to check out, 'b' to go back, 'x' to exit.")
                row += 2
                self.view_cart(row)

                try:
                    next_step = bytes.decode(self.screen.getstr(15, 40, 60))
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
                            if next_step >= 0 and next_step <= len(product_list):
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
                row += 1
                self.screen.addstr(row, 12, "Press 'b' to go back and choose a login option, or x to exit.")

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
            product_name = get_product_from_db(prod_ID)
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
                    for i in range(quantity):
                        generate_new_line_item(self.cart_id, prod_ID)
                    row += 3
                    self.screen.addstr(row, 40, str(quantity) + " " + product_name + " added to cart.")
                    row += 3
                    self.screen.addstr(row, 40, "Press 'any key' to return to shopping menu.")

                    quantity = chr(self.screen.getch())
                    self.shop_menu()

                    # print(quantity + item_to_add["name"] + " added to cart.")
                    # self.shop_menu()

        def view_cart(self, row_start):
            """
            Displays the cart of the currently logged in user. Handles what to say if the user does not have a cart or if their cart is empty.
            ========
            Method Arguments: None
            """

            # check if user has a cart.
            try:
                self.cart_id = check_if_cart_exists(self.current_user)
            except TypeError:
                pass
            if self.cart_id is None:
                # if they don't have a cart, create one and print "your cart is empty, start shopping"
                self.cart_id = new_order(self.current_user)
                self.screen.addstr(row_start, 40, "Your cart is empty. Start shopping!")
                row_start += 1
            else:
                cart_to_print = build_cart_view(self.cart_id)
                # if they have a cart, check if cart is not empty.
                if len(cart_to_print) == 0:
                    self.screen.addstr(row_start, 40, "Your cart is empty. Start shopping!")
                    row_start += 1
                else:
                    # if it's not empty, print it.
                    # format for columns
                    row_string = "{0:<18}{1:<11}${2:<14}"
                    total_string = "{0:<29}${1:<14}"
                    heading_string = "{0:<29}{1:<14}"
                    total_list = []
                    self.screen.addstr(row_start, 40, heading_string.format("Your cart:", "Totals:"))
                    row_start += 1
                    self.screen.addstr(row_start, 40, "*" * 44)
                    row_start += 1
                    # loop over cart items and calculate total (grab price from 'products.txt')
                    for item in cart_to_print:
                        # append total to list of totals (for amount due calculation)
                        total_list.append(item[2])
                        # limit product name
                        product_name = (item[0] if len(item[0]) <= 17 else item[0][:14] + "...") + " "
                        # print
                        self.screen.addstr(row_start, 40, row_string.format(product_name, item[1], item[2]))
                        row_start += 1
                    self.screen.addstr(row_start, 40, "*" * 44)
                    row_start += 1
                    # self.screen.addstr out total amount due
                    self.screen.addstr(row_start, 40, total_string.format("Order total:", sum(total_list)))

        def convert_to_completed(self, payment_uid):
            # add payment id to customers open order, direct to logged-in menu
            add_payment_to_order(self.current_user, payment_uid)
            self.cart_id = None
            self.show_purchased_menu()

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
                        if next_step >= 0 and next_step <= len(payment_list):
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

            report_list = return_report_line_items()
            total_list = return_report_totals()

            heading_string = "{0:<18}{1:<11}{2:<11}{3:<15}"
            row_string = "{0:<18}{1:<11}{2:<11}${3:<14}"
            total_string = "{0:<18}{1:<11}{2:<11}${3:<14}"

            # ######### PRINT REPORT ##########
            row = 5

            self.screen.addstr(row, 40, heading_string.format("Products", "Orders", "Customers", "Revenue"))
            row += 1
            self.screen.addstr(row, 40, "*" * 55)
            row += 1

            for report_row in report_list:
                # limit display names/values
                product_name = (report_row[0] if len(report_row[0]) <= 17 else report_row[0][:14] + "...") + " "
                order = (str(report_row[1]) if len(str(report_row[1])) <= 11 else str(report_row[1])[:8] + "...") + " "
                customers = (str(report_row[2]) if len(str(report_row[2])) <= 11 else str(report_row[2])[:8] + "...")
                revenue = (str(str(report_row[3])) if len(str(str(report_row[3]))) <= 14 else str(report_row[3])[:11] + "...")
                # add row to screen
                self.screen.addstr(row, 40, row_string.format(product_name, order, customers, revenue))
                # increment row by 1
                row += 1

            # limit totals display
            order_sum = (str(total_list[0][0]) if len(str(total_list[0][0])) <= 17 else str(total_list[0][0])[:14] + "...") + " "
            customer_sum = (str(total_list[0][1]) if len(str(total_list[0][1])) <= 11 else str(total_list[0][1])[:8] + "...")
            revenue_sum = (str(total_list[0][2]) if len(str(total_list[0][2])) <= 14 else str(total_list[0][2])[:11] + "...")
            self.screen.addstr(row, 40, "*" * 55)
            row += 1
            # add row to screen
            self.screen.addstr(row, 40, total_string.format("Totals:", order_sum, customer_sum, revenue_sum))
            # increment row by 1
            row += 2

            self.screen.addstr(row, 40, "Press any key to continue")
            choice = chr(self.screen.getch())
            if self.current_user is not None:
                self.logged_in_menu()
            else:
                self.unlogged_in_menu()

        def verify_admin_menu(self):
            """
            Login verification for admin privileges
            """
            admin_id = get_param('What is your admin ID?', self.screen)
            password = get_param('What is your password?', self.screen)

            admin = verify_admin(admin_id, password)

            if admin:
                self.screen.clear()
                self.screen.border(0)
                self.screen.addstr(12, 40, 'Logged in successfully as admin.')
                self.screen.addstr(13, 40, 'Press any key to continue.')
                self.screen.refresh()

                pause = chr(self.screen.getch())
                self.admin_menu()
            else:
                self.screen.clear()
                self.screen.border(0)
                self.screen.addstr(12, 40, 'Admin login failed.')
                self.screen.addstr(13, 40, 'Press any key to continue.')
                self.screen.refresh()

                pause = chr(self.screen.getch())
                self.unlogged_in_menu()

        def admin_menu(self):
            """
            Menu for admin privileges
            """
            self.screen.clear()
            self.screen.border(0)
            self.screen.addstr(12, 40, '1. Add new product')
            self.screen.addstr(13, 40, '2. Logout admin')
            self.screen.refresh()

            choice = str(chr(self.screen.getch()))

            if choice == '1':
                name = get_param('What is the name of the product?', self.screen)
                price = int(get_param('What is the price of the product?', self.screen))

                success = add_new_product(name, price)

                if success:
                    self.screen.clear()
                    self.screen.border(0)
                    self.screen.addstr(12, 40, 'Product added successfully!')
                    self.screen.addstr(13, 40, 'Press any key to continue.')

                    pause = chr(self.screen.getch())
                    self.admin_menu()

                else:
                    self.screen.clear()
                    self.screen.border(0)
                    self.screen.addstr(12, 40, 'There was a problem adding that product.')
                    self.screen.addstr(13, 40, 'Press any key to continue.')

                    pause = chr(self.screen.getch())
                    self.admin_menu()

            elif choice == '2':
                self.screen.clear()
                self.screen.border(0)
                self.screen.addstr(12, 40, 'Logged out admin.')
                self.screen.addstr(13, 40, 'Press any key to continue.')

                pause = chr(self.screen.getch())
                self.unlogged_in_menu()


        def show_purchased_menu(self):
            """
            Shows the most recently purchased items in a curses menu
            """

            self.screen.clear()
            self.screen.border(0)
            result = get_last_order_for_menu()
            self.screen.addstr(6, 40, "Order complete. Press any key to continue")
            row = 8
            total = 0

            for entry in result:
                self.screen.addstr(row, 40, "{0} - {1}".format(entry[1], entry[2]))
                total += int(entry[2])
                row += 1
            row += 2
            self.screen.addstr(row, 40, "Total = {0}".format(total))
            pause = self.screen.getch()
            return self.logged_in_menu()

    if __name__ == '__main__':
        app = Meow()
        app.unlogged_in_menu()

except KeyboardInterrupt:
    curses.endwin()
