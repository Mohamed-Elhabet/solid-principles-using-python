
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
    
    

class Square:
    def __init__(self, side: float):
        self._side = side
        
    def set_side(self, side: float):
        self._side = side
        
    def get_area(self) -> float:
        return self._side * self._side
    
    
def calculate_rectangle_area(rectangle: Rectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    return rectangle.get_area()


def calculate_square_area(square: Square):
    square.set_side(5)
    return square.get_area()

rect = Rectangle(2, 3)
sq = Square(2)

print(calculate_rectangle_area(rect))
print(calculate_square_area(sq))

