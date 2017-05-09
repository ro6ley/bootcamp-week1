import unittest
from oop import Safaricom, Airtel


class MobileNetworksTestCases(unittest.TestCase):
    def setUp(self):
        new_saf = Safaricom()
        new_airtel = Airtel()

    def test_buy_airtime(self):
        """
        Check whether purchase of airtime updates the balance
        """
        # For safaricom
        self.new_saf.balance = 0
        self.new_saf.buy_airtime(40)
        self.assertEqual(self.new_saf.balance, 40)
        # For airtel
        self.new_airtel.balance = 0
        self.new_airtel.buy_airtime(32)
        self.assertEqual(self.new_airtel.balance, 32)

    def test_send_airtime(self):
        """
        Check whether sending airtime reduces balance by that amount
        and raises error if amount not sufficient
        """
        # For Safaricom

        # For Airtel