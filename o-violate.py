
class PaymentProcessor:
    def process_payment(self, payment_type: str, amount: float):
        if payment_type == 'credit_card':
            self.process_credit_card_payment(amount)
        elif payment_type == 'paypal':
            self.process_paypal_payment(amount)
        else:
            raise ValueError('Unsupported payment type')
        
        
    def process_credit_card_payment(self, amount: float):
        print(f'Processing credit card payment of ${amount}')
        
    
    def process_paypal_payment(self, amount: float):
        print(f'Processing PayPal payment of ${amount}')
        