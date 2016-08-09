from meow import *
import unittest

# NOTE: I have not assigned any passed-in arguments here. You guys do that.


class test_utility(unittest.TestCase):
    # HEY pass in test .txt files.
    def test_get_value_returns_none_when_not_found(self):
        self.assertIsNone(get_value('data/test/test_order.txt', 'fake_uid'))

    def test_get_value_returns_class_object_when_found(self):
        test_obj = get_value('data/test/test_order.txt', 'b91265d9-2dd1-4909-95db-bb2b4245d939')
        self.assertIsNotNone(test_obj)
        self.assertIsInstance(test_obj, Order)

    def test_add_new_item(self):
        oid = '123'
        test_obj = Order(oid)
        returned_oid = add_to_file('data/test/test_order.txt', test_obj)

        added_obj = get_value('data/test/test_order.txt', returned_oid)
        self.assertIsInstance(added_obj, Order)
        self.assertEqual(added_obj.customer_id, '123')
        self.assertEqual(added_obj.payment, None)

        # Clean up (delete the item just added)
        lib = deserialize('data/test/test_order.txt')
        del lib[returned_oid]
        serialize('data/test/test_order.txt', lib)

class test_product(unittest.TestCase):

    def test_generate_product_list(self):
        # list of all the products.
        pass


class test_customer(unittest.TestCase):

    def test_generate_new_customer(self):
        pass

    def test_generate_customer_list(self):
        pass


class test_payment(unittest.TestCase):

    def test_generate_new_payment(self):
        pass

    def test_generate_payment_options_list(self):
        pass


class test_temp_cart(unittest.TestCase):

    def test_generate_new_cart(self):
        pass

    def test_view_cart(self):
        pass

    def test_add_item_to_cart(self):
        pass


class test_order(unittest.TestCase):

    def test_generate_new_order(self):
        pass

    def test_add_product_to_order(self):
        # adding productID as key, quantity as value.
        # please also test adding another of the same object to the order.
        pass


class test_line_item(unittest.TestCase):

    def test_generate_new_line_item(self):
        pass

    def test_generate_line_items_view(self):
        # get a dictionary of ALL the line items, for the report. key: line item UID. value: {order id: **, product id: **}
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
