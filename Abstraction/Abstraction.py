
from abc import ABC, abstractmethod

class Car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount:",amount)
        @abstractmethod
        def payment(self, amount):
            pass


class CreditCardPayment(Car):
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))


obj = CreditCardPayment()
obj.paySlip("$600")
obj.payment("$600")
