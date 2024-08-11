
class EmailSender:
    def send_email(self, message: str, recipient: str):
        print(f'Sending email to {recipient}: {message}')
        

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()
        
    def send_notification(self, message: str, recipient: str):
        self.email_sender.send_email(message, recipient)
        


service = NotificationService()
service.send_notification('Hello world', 'test@test.com')

