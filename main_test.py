from meow import *
import unittest


class test_utility(unittest.TestCase):
    # HEY pass in test .txt files.
    def test_get_value_returns_none_when_not_found(self):
        self.assertIsNone(get_value('data/test/test_order.txt', 'fake_uid'))

    def test_get_value_returns_class_object_when_found(self):
        test_obj = get_value('data/test/test_order.txt', '9a4618fa-88d3-43e2-8556-7de4295deef3')
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
        self.assertIsInstance(generate_product_list("./data/products"), dict)
        # need more tests


class test_customer(unittest.TestCase):

    def test_generate_new_customer(self):
        test_object = instantiate_customer_object("megan", "1234 User Lane", "Franklin", "Tennessee", "37067", "555-5555")
        # the customer object is instantiated.
        self.assertIsInstance(test_object, Customer_Object)
        # the arguments get passed correctly.
        self.assertEqual(test_object.name, "megan")
        self.assertEqual(test_object.address, "1234 User Lane")
        self.assertEqual(test_object.city, "Franklin")
        self.assertEqual(test_object.state, "Tennessee")
        self.assertEqual(test_object.zipcode, "37067")
        self.assertEqual(test_object.phone, "555-5555")

        # the overarching generation function returns a string value. It'll be a unique ID. Test for whether the values get serialized correctly is below, in generate_customer_list.
        self.assertEqual(type(generate_new_customer("data/test/test_customer.txt", "chase", "1234 Sesame Street", "Nashville", "Tennessee", "37067", "555-5555")), str)

    def test_generate_customer_menu(self):
        uid = generate_new_customer("data/test/test_customer.txt", "name", "address", "city", "state", "zipcode", "phone")
        # if you request a customer menu it returns a dictionary. The key of '1' is in it.
        self.assertIsInstance(generate_customer_menu("data/test/test_customer.txt"), dict)
        self.assertIn(1, generate_customer_menu("data/test/test_customer.txt").keys())
        # Add a customer, and then test.customer.txt has that customer ID as a value when you request the list.
        lib = generate_customer_menu("data/test/test_customer.txt")
        self.assertIn(uid, lib.values())


class test_payment(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.payment_id = generate_new_payment("data/test/test_payments.txt", "Visa", 11223344, 1234)
        self.payment_obj = get_value("data/test/test_payments.txt", self.payment_id)

    def test_generate_new_payment(self):
        self.assertIsInstance(self.payment_obj, Payment_Object)
        self.assertEqual(self.payment_obj.name, "Visa")
        self.assertEqual(self.payment_obj.account_number, 11223344)
        self.assertEqual(self.payment_obj.customer, 1234)

    def test_generate_payment_options_list(self):
        payments_dict = generate_payments_menu("data/test/test_payments.txt", 1234)
        self.assertIn(self.payment_id, payments_dict.values())


class test_temp_cart(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sample_user = generate_new_customer("data/test/test_customer.txt", "megan", "1234 user lane", "franklin", "tennessee", "37067", "555-5555")

    def test_cart_default(self):
        # when you create a user, it makes an empty cart property.
        user_obj = get_value("data/test/test_customer.txt", self.sample_user)
        self.assertEqual(user_obj.cart, {})

    def test_add_item_to_cart(self):
        # item adds correctly to cart.
        add_item_to_cart("data/test/test_customer.txt", self.sample_user, "product_id", 2)
        user_obj = get_value("data/test/test_customer.txt", self.sample_user)
        self.assertIn("product_id", user_obj.cart.keys())
        self.assertEqual(2, user_obj.cart["product_id"])

        # if you add more of the same item to the cart, it adds the total together.
        add_item_to_cart("data/test/test_customer.txt", self.sample_user, "product_id", 1)
        user_obj = get_value("data/test/test_customer.txt", self.sample_user)
        self.assertEqual(user_obj.cart["product_id"],  3)

        # if you add a different item to the cart, it adds it with the correct quantity, and the first item is still there.
        add_item_to_cart("data/test/test_customer.txt", self.sample_user, "another_product_id", 1)
        user_obj = get_value("data/test/test_customer.txt", self.sample_user)
        self.assertEqual(3, user_obj.cart["product_id"])
        self.assertEqual(1, user_obj.cart["another_product_id"])

        # if you empty your cart, it's still there just empty.
        delete_cart("data/test/test_customer.txt", self.sample_user)
        user_obj = get_value("data/test/test_customer.txt", self.sample_user)
        self.assertEqual(user_obj.cart, {})


class test_order(unittest.TestCase):

    def test_generate_new_order(self):
        # This test is almost exactly the same as 'test_add_new_item';
        # It simply checks that the values passed through this generate order
        # function create the order and add it to the order library as expected
        cid = '123'
        pid = '456'
        returned_oid = new_order(cid, pid, 'data/test/test_order.txt')

        cid_2 = '222'
        pid_2 = '444'
        second_oid = new_order(cid_2, pid_2, 'data/test/test_order.txt')

        added_obj = get_value('data/test/test_order.txt', returned_oid)
        self.assertIsInstance(added_obj, Order)
        self.assertEqual(added_obj.customer_id, '123')
        self.assertEqual(added_obj.payment, '456')

        # Clean up (delete the item just added)
        lib = deserialize('data/test/test_order.txt')
        del lib[returned_oid]
        del lib[second_oid]
        serialize('data/test/test_order.txt', lib)

    def test_build_temp_customer_orders_dict(self):
        cid = '123'
        pid = '456'
        returned_oid = new_order(cid, pid, 'data/test/test_order.txt')

        order_lib = build_order_dict('data/test/test_order.txt', '123')
        check_lib = [(item.customer_id == '123') for key, item in order_lib.items()]
        self.assertFalse(False in check_lib)

        # Clean up (delete the item just added)
        lib = deserialize('data/test/test_order.txt')
        del lib[returned_oid]
        serialize('data/test/test_order.txt', lib)


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
