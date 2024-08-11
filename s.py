class Book:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content
        
    def get_details(self) -> str:
        return f'Title: {self.title}, Author: {self.author}'
    
    

class FileManager:
    @staticmethod
    def save_to_file(filename: str, content: str):
        with open(filename, 'w') as file:
            file.write(content)
            
            

class Printer:
    @staticmethod
    def print_content(content: str):
        print(content)
        

book = Book("The Python Journey", "Jane Doe", "Once upon a time in Python...")
print(book.get_details())

FileManager.save_to_file('book2.txt', book.content)
Printer.print_content(book.content)
