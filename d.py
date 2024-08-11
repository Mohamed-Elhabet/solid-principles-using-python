
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str):
        ...
        

class EmailSender(MessageSender):
    def send(self, message: str, recipient: str):
        print(f'Sending email to {recipient} : {message}')
        
    
class SMSSender(MessageSender):
    def send(self, message: str, recipient: str):
        print(f'Sending SMS to {recipient} : {message}')
        
        
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender
        
    def send_notification(self, message: str, recipient: str):
        self.sender.send(message, recipient)
        
        
email_service = NotificationService(EmailSender())
email_service.send_notification('Hello Email', 'test@test.com')


sms_service = NotificationService(SMSSender())
sms_service.send_notification('Hello via sms', '+1425654558')


# Example with Dependency Injection:

class PushNotificationSender(MessageSender):
    def send(self, message: str, recipient: str):
        print(f'sending push notification to {recipient} : {message}')
        
        
# Injecting different types of senders
push_service = NotificationService(PushNotificationSender())
push_service.send_notification('Hello via push notification', 'device_token')


