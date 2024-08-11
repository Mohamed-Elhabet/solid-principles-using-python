# The Single Responsibility Principle (SRP)


class Book:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content
        
    
    def get_details(self) -> str:
        return f'Title: {self.title}, Author: {self.author}'
    
    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            file.write(self.content)
            
    def print_content(self):
        print(self.content)
        
        
book = Book('The python journey', 'Jane Doe', 'Once upon a time in python')
print(book.get_details())
book.save_to_file('book.txt')
book.print_content()