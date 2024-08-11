
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass
    
    
    def hello(self):
        print("HELLO")
    

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f'Processing credit card payment of ${amount}')
        
        
class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f'Processing PayPal payment of ${amount}')
        
     

payment_methods = [
    CreditCardPaymentProcessor(),
    PayPalPaymentProcessor()
]

for processor in payment_methods:
    processor.process_payment(100.0)
    
    

# Adding a new payment method
class BitcoinPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f'Processing Bitcoin payment of ${amount}')
        
        

payment_methods.append(BitcoinPaymentProcessor())

for processor in payment_methods:
    processor.process_payment(200.0)
        