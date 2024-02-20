class Shape:
    def __init__(self, name):
        self.name = name

class Color:
    def __init__(self, color):
        self.color = color

class ColoredShape(Shape, Color):
    def __init__(self, name, color):
        # Call the constructors of the parent classes
        Shape.__init__(self, name)
        Color.__init__(self, color)

# Example usage:
colored_shape = ColoredShape(name="Square", color="Red")
print(f"Shape: {colored_shape.name}, Color: {colored_shape.color}")
