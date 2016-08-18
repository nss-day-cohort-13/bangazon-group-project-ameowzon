from meow import *
import unittest


class test_utility(unittest.TestCase):

    def test_set_thing(self):
        thing = set_thing([(2, "special thing"), (4, "not as special thing"), (6, "nope")], 2)
        self.assertEqual(thing, 4)
        thing2 = set_thing([(2, "special thing"), (4, "not as special thing"), (6, "nope")], 200)
        self.assertEqual(thing2, None)


class test_product(unittest.TestCase):

    def test_read_product_from_db(self):
        thing = read_product_from_db()
        self.assertEqual(thing[1], True)
        product_list = thing[0]
        self.assertIsInstance(product_list, list)
        self.assertIsInstance(product_list[0], tuple)
        self.assertNotEqual(len(product_list), 0)
        self.assertEqual(len(product_list[0]), 3)
        self.assertIsInstance(product_list[0][0], int)
        self.assertIsInstance(product_list[0][1], str)
        self.assertIsInstance(product_list[0][2], int)

    def test_get_product_from_db(self):
        thing = get_product_from_db(1)
        self.assertIsInstance(thing, str)
        self.assertEqual(thing, "Sheer Kahn")


class test_customer(unittest.TestCase):

    def test_generate_new_customer(self):
        thing = generate_new_customer("Amy", "111 street", "nash", "Tn", "44444", "5555555")
        self.assertIsInstance(thing, int)

    def test_get_customer_name(self):
        thing = get_customer_name(1)
        self.assertIsInstance(thing, str)
        thing2 = get_customer_name(600)
        self.assertEqual(thing2, None)

    def test_generate_customer_menu(self):
        thing = generate_customer_menu()
        self.assertEqual(thing[1], False)
        user_list = thing[0]
        self.assertIsInstance(user_list, list)
        self.assertIsInstance(user_list[0], tuple)
        self.assertNotEqual(len(user_list), 0)
        self.assertEqual(len(user_list[0]), 2)
        self.assertIsInstance(user_list[0][0], int)
        self.assertIsInstance(user_list[0][1], str)


class test_payment(unittest.TestCase):

    def test_generate_new_payment(self):
        thing = generate_new_payment("Visa", "3", 4)
        self.assertIsInstance(thing, int)

    def test_generate_payment_menu(self):
        thing = generate_payments_menu(2)
        self.assertEqual(thing[1], False)
        payment_list = thing[0]
        self.assertIsInstance(payment_list, list)
        self.assertIsInstance(payment_list[0], tuple)
        self.assertNotEqual(len(payment_list), 0)
        self.assertEqual(len(payment_list[0]), 2)
        self.assertIsInstance(payment_list[0][0], int)
        self.assertIsInstance(payment_list[0][1], str)


class test_cart_handler(unittest.TestCase):

    def test_check_if_cart_exists(self):
        order_num = new_order(1)
        thing = check_if_cart_exists(1)
        self.assertIsInstance(thing, int)
        thing2 = check_if_cart_exists(60000)
        self.assertEqual(thing2, None)

    def test_build_cart_view(self):
        order_num = new_order(1)
        generate_new_line_item(order_num, 2)
        generate_new_line_item(order_num, 5)
        thing = build_cart_view(order_num)
        self.assertIsInstance(thing, list)
        self.assertIsInstance(thing[0], tuple)
        self.assertNotEqual(len(thing), 0)
        self.assertEqual(len(thing[0]), 3)
        self.assertIsInstance(thing[0][0], str)
        self.assertIsInstance(thing[0][1], int)
        self.assertIsInstance(thing[0][2], int)


class test_order(unittest.TestCase):

    def test_generate_new_order(self):
        order_num = new_order(1)
        self.assertIsInstance(order_num, int)

    def test_add_payment_to_order(self):
        # I don't know if we can test this since it's not returning anything.
        pass

    def test_get_last_order_for_menu(self):
        product_list = get_last_order_for_menu()
        pass


class test_line_item(unittest.TestCase):

    def test_generate_new_line_item(self):
        # I don't think we can test this since it's not returning anything.
        pass

    def test_return_report_line_items(self):
        thing = return_report_line_items()
        self.assertIsInstance(thing, list)
        self.assertIsInstance(thing[0], tuple)
        self.assertEqual(len(thing[0]), 4)
        self.assertIsInstance(thing[0][0], str)
        self.assertIsInstance(thing[0][1], int)
        self.assertIsInstance(thing[0][2], int)
        self.assertIsInstance(thing[0][3], int)
        pass

    def test_return_report_totals(self):
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
