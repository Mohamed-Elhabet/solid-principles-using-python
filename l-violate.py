
class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
        
    def set_width(self, width: float):
        self._width = width
        
    def set_height(self, height: float):
        self._height = height
        
    def get_area(self) -> float:
        return self._width * self._height
    

class Square(Rectangle):
    def set_width(self, width: float):
        self._width = width    
        self._height = width
        
    
    def set_height(self, height: float):
        self._height = height
        self._width = height
        

def calculate_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    return rectangle.get_area()


rect = Rectangle(2, 3)
sq = Square(2, 2)

print(calculate_area(rect))  # 50
print(calculate_area(sq))    # Expected 50, but gets 100

