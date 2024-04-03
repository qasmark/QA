class PaymentSystem:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.commission_rate = 0.05 
        self.status = None

    def check_balance(self):
        return self.balance

    def make_payment(self, amount):
        total_amount = amount * (1 + self.commission_rate)
        if self.balance >= total_amount:
            self.balance -= total_amount
            self.status = "Success"
            return True
        else:
            self.status = "Insufficient funds"
            return False

    def add_funds(self, amount):
        self.balance += amount

    def set_commission_rate(self, rate):
        if rate <= 0:
            self.status = "Negative commission"
            rate = 0
        else:
            self.commission_rate = rate

    def get_status(self):
        return self.status
