import unittest
from oop import Safaricom, Airtel


class MobileNetworksTestCases(unittest.TestCase):
    def setUp(self):
        self.new_saf = Safaricom(0)
        self.new_airtel = Airtel(0)

    def test_buy_airtime(self):
        """
        Check whether purchase of airtime updates the balance
        """
        # For safaricom
        self.new_saf.buy_airtime(40)
        self.assertEqual(self.new_saf.balance, 40)
        # For airtel
        self.new_airtel.buy_airtime(32)
        self.assertEqual(self.new_airtel.balance, 32)

    def test_send_airtime(self):
        """
        Check whether sending airtime reduces balance by that amount
        and raises error if amount not sufficient
        """
        # For Safaricom
        self.new_saf.buy_airtime(40)
        self.new_saf.send_airtime(32)
        self.assertEqual(self.new_saf.balance, 8)
        self.assertEqual(self.new_saf.send_airtime(20), "Insufficient balance")
        # For Airtel
        self.new_airtel.buy_airtime(32)
        self.new_airtel.send_airtime(20)
        self.assertEqual(self.new_airtel.balance, 12)
        self.assertEqual(self.new_airtel.send_airtime(20), "Insufficient balance")

    def test_invalid_inputs(self):
        """
        Check whether the methods raise errors if the input is not an integer
        """
        # For Safaricom
        self.assertEqual(self.new_saf.send_airtime("40"), "Only integers allowed")
        self.assertEqual(self.new_saf.buy_airtime("40"), "Only integers allowed")

        # For Airtel
        self.assertEqual(self.new_airtel.send_airtime("40"), "Only integers allowed")
        self.assertEqual(self.new_airtel.buy_airtime("40"), "Only integers allowed")

if __name__ == "__main__":
    unittest.main()
    