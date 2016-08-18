from meow import *
import unittest


class test_utility(unittest.TestCase):

    def test_set_thing(self):
        pass


class test_product(unittest.TestCase):

    def read_product_from_db(self):
        pass

    def generate_product_list(self):
        pass


class test_customer(unittest.TestCase):

    def test_generate_new_customer(self):
        pass

    def test_get_customer_name(self):
        pass

    def test_generate_customer_menu(self):
        pass


class test_payment(unittest.TestCase):

    def test_generate_new_payment(self):
        pass

    def test_generate_payment_options_list(self):
        pass


class test_cart_handler(unittest.TestCase):

    def test_build_cart_view(self):
        pass

    def test_delete_cart(self):
        pass

    def test_check_if_cart_exists(self):
        pass


class test_order(unittest.TestCase):

    def test_generate_new_order(self):
        pass

    def test_add_payment_to_order(self):
        pass


class test_line_item(unittest.TestCase):

    def test_generate_new_line_item(self):
        pass

    def test_return_report_line_items(self):
        pass

class test_meow(unittest.TestCase):

    def test_user_reset(self):
        pass

    def test_convert_cart_to_order(self):
        pass

    def test_set_current_user(self):
        pass

    def test_set_payment(self):
        pass
        # note this gets passed directly into convert card to order... maybe move it to the payment handler.

    def test_calculate_cart_totals(self):
        pass

    def test_generate_report(self):
        # not testing the actual printer, but we need to make sure the numbers output correctly. This should be the last thing we test.
        pass

if __name__ == '__main__':
    unittest.main()
