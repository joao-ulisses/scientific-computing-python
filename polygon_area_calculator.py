class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        result = ''
        for h in range(self.height):
            result += f'{"":*^{self.width}}\n'
        return result

    def get_amount_inside(self, shape):
        times = 0 
        if (shape.width < self.width) and (shape.height < self.height):
            times = (self.height // shape.height)*(self.width // shape.width)
            return times
        else:
            times = 0 
        return times
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f'Square(side={self.width})'

r1 = Rectangle(5, 5)
print(r1.get_picture())
s1 = Square(10)
s1.set_height(51)
print(Rectangle(15,10).get_amount_inside(Square(5)))