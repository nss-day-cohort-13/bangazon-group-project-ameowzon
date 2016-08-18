from meow import *
import unittest


class test_utility(unittest.TestCase):

    def test_set_thing(self):
        pass


class test_product(unittest.TestCase):

    def read_product_from_db(self):
        thing = read_product_from_db()
        self.assertIsInstance(thing, list)
        self.assertIsInstance(thing[0], tuple)
        self.assertNotEqual(len(thing), 0)
        self.assertIsInstance(thing[0][0], int)
        self.assertIsInstance(thing[0][1], str)
        self.assertIsInstance(thing[0][2], int)


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
        thing = return_report_totals()
        self.assertIsInstance(thing, list)
        self.assertIsInstance(thing[0], tuple)
        self.assertEqual(len(thing[0]), 3)
        self.assertIsInstance(thing[0][0], int)
        self.assertIsInstance(thing[0][1], int)
        self.assertIsInstance(thing[0][2], int)


class test_meow(unittest.TestCase):

    def test_init(self):
        self.meow_test = Meow()
        self.assertEqual(self.meow_test.current_user, None)
        self.assertEqual(self.meow_test.user_name, "")
        self.assertEqual(self.meow_test.cart_id, None)

    def test_user_reset(self):
        self.meow_test = Meow()
        self.meow_test.user_name = "megan"
        self.meow_test.current_user = 4
        self.meow_test.cart_id = 6
        self.meow_test.reset_user()

        self.assertEqual(self.meow_test.current_user, None)
        self.assertEqual(self.meow_test.user_name, "")
        self.assertEqual(self.meow_test.cart_id, None)


if __name__ == '__main__':
    unittest.main()
