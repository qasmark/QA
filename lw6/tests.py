import unittest
from payment_system import PaymentSystem

'''
coverage report -m
coverage run -m unittest tests.py
'''
class TestPaymentSystem(unittest.TestCase):
    def setUp(self):
        self.payment_system = PaymentSystem(initial_balance=100)

    def test_check_balance(self):
        expected_balance = 100
        
        actual_balance = self.payment_system.check_balance()
        
        self.assertEqual(actual_balance, expected_balance, "Incorrect balance after initialization")

    def test_make_payment_sufficient_funds(self):
        payment_amount = 50
        expected_balance = 47.5
        
        result = self.payment_system.make_payment(payment_amount)
        
        self.assertTrue(result, "Payment failed despite sufficient funds")
        self.assertEqual(self.payment_system.balance, expected_balance, "Incorrect balance after successful payment")


        
    def test_make_payment_all_funds(self):
        payment_amount = 95.238095
        expected_balance = 0.0
        
        result = self.payment_system.make_payment(payment_amount)
        
        self.assertTrue(result, "Payment failed despite sufficient funds")
        self.assertEqual(round(self.payment_system.balance, 2), expected_balance, "Incorrect balance after successful payment")


    def test_make_payment_insufficient_funds(self):
        payment_amount = 150
        expected_balance = 100
        expected_status = "Insufficient funds"
        
        result = self.payment_system.make_payment(payment_amount)
        
        self.assertFalse(result, "Payment succeeded despite insufficient funds")
        self.assertEqual(self.payment_system.balance, expected_balance, "Balance changed despite insufficient funds")
        self.assertEqual(self.payment_system.status, expected_status, "Incorrect status after failed payment")

    def test_add_funds(self):
        added_amount = 50
        expected_balance = 150
        
        self.payment_system.add_funds(added_amount)
        
        self.assertEqual(self.payment_system.balance, expected_balance, "Incorrect balance after adding funds")

    def test_set_commission_rate(self):
        new_commission_rate = 0.1
        
        self.payment_system.set_commission_rate(new_commission_rate)

        self.assertEqual(self.payment_system.commission_rate, new_commission_rate, "Commission rate not set correctly")

    def test_get_status(self):
        expected_status = None
        
        actual_status = self.payment_system.get_status()
        
        self.assertEqual(actual_status, expected_status, "Incorrect initial status")
    
    def setUp(self):
        self.payment_system = PaymentSystem(initial_balance=100)

    def test_make_payment_invalid_type(self):
        invalid_amounts = ["50", 50.0, {"amount": 50}]

        for invalid_amount in invalid_amounts:
            with self.subTest(invalid_amount=invalid_amount):
                with self.assertRaises(TypeError):
                    self.payment_system.make_payment(invalid_amount, "Invalid type of amount")

    def test_add_funds_invalid_type(self):
        invalid_amounts = ["50", 50.0, {"amount": 50}]

        for invalid_amount in invalid_amounts:
            with self.subTest(invalid_amount=invalid_amount):
                with self.assertRaises(TypeError):
                    self.payment_system.add_funds(invalid_amount, "Invalid type of adding funds")

    def test_set_commission_rate_invalid_type(self):
        invalid_rates = ["0.1", 0.1, {"rate": 0.1}]

        for invalid_rate in invalid_rates:
            with self.subTest(invalid_rate=invalid_rate):
                with self.assertRaises(TypeError):
                    self.payment_system.set_commission_rate(invalid_rate, "Invalid type of rate")

if __name__ == '__main__':
    unittest.main()
