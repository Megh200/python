from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw(self):
        pass  # Complete this method in subclasses

# Example subclass
class Circle(Shape):
    def draw(self):
        print(f"Drawing a circle named {self.name}")

# Example usage:
circle = Circle(name="MyCircle")
circle.draw()
