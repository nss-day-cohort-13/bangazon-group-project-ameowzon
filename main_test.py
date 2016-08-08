from meow import *
import unittest


class test_meow(unittest.TestCase):
    def test_user_reset(self):
        pass
    def test_convert_card_to_order(self):
        pass
    def test_set_current_user(self):
        pass
    def test_set_payment(self):
        pass
        # note this gets passed directly into convert card to order... maybe move it to the payment handler.
    def test_generate_report(self):
        pass
    def test_calculate_cart_totals(self):
        pass


class test_utility(unittest.TestCase):
    def test_get_value(self):
        pass
    def test_add_new_item(self):
        #generate a UID here.
        #deserialize, add new item to library, reserialize. return UID.
        pass


class test_temp_cart(unittest.TestCase):
    def test_generate_new_cart(self):
        pass
    def test_view_cart(self):
        pass
    def test_add_item_to_cart(self):
        pass


class test_line_item(unittest.TestCase):
    def test_generate_new_line_item(self):
        pass
    def test_generate_line_items_list(self):
        # get a list of ALL the line items, for the report.
        pass


class test_order(unittest.TestCase):
    def test_generate_new_order(self):
        pass
    def test_add_product_to_order(self):
        pass


class test_product(unittest.TestCase):
    def test_generate_product_list(self):
        pass
    def test_add_product(self):
        # may not need to test this since chase is the only one using it.
        pass


class test_payment(unittest.TestCase):
    def test_generate_new_payment(self):
        pass
    def test_generate_payment_options_list(self):
        pass


class test_customer(unittest.TestCase):
    def test_generate_new_customer(self):
        pass
    def test_generate_customer_list(self):
        pass


if __name__ == '__main__':
    unittest.main()
