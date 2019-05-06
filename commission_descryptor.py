class Value:
    def __init__(self):
        self.value = None

    def __set__(self, instance, value):
        self.value = self.subtract_commission(instance, value)

    @staticmethod
    def subtract_commission(self, value):
        return value - self.commission * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount.value)
