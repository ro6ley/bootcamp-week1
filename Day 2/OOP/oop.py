class MobileNetworks(object):
    """
    Class for the general mobile networks
    """
    def buy_airtime(self, amount):
        pass

    def send_airtime(self, amount):
        pass


class Safaricom(MobileNetworks):
    """
    Class for the Safaricom object
    """
    def __init__(self, balance):
        self.balance = balance

    def buy_airtime(self, amount):
        """
        Method to buy airtime
        """
        if isinstance(amount, int) and amount is not None:
            if amount >= 0:
                self.balance += amount
                return self.balance
            else:
                return "Error: Invalid amount"
        else:
            return "Only integers allowed"

    def send_airtime(self, amount):
        """
        Method to send airtime
        """
        if isinstance(amount, int) and amount is not None:
            if amount >= 0:
                if (self.balance - amount) > 5:
                    self.balance -= amount
                    return self.balance
                else:
                    return "Insufficient balance"
            else:
                return "Invalid amount entered"
        else:
            return "Only integers allowed"


class Airtel(MobileNetworks):
    """Class for the Airtel object"""
    def __init__(self, balance):
        self.balance = balance

    def buy_airtime(self, amount):
        """
        Method to buy airtime
        """
        if isinstance(amount, int) and amount is not None:
            if amount >= 0:
                self.balance += amount
                return self.balance
            else:
                return "Error: Invalid amount"
        else:
            return "Only integers allowed"

    def send_airtime(self, amount):
        """
        Method to send airtime
        """
        if isinstance(amount, int) and amount is not None:
            if amount >= 0:
                if (self.balance - amount) > 5:
                    self.balance -= amount
                    return self.balance
                else:
                    return "Insufficient balance"
            else:
                return "Invalid amount entered"
        else:
            return "Only integers allowed"
