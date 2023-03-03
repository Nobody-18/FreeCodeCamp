class Rectangle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return (self.height * self.width)

    def get_perimeter(self):
        return (2 * (self.height + self.width))

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return ("Too big for picture")
        picture = ""
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += ("\n")

        return picture

    def get_amount_inside(self, Rectangle):
        w = self.width // Rectangle.width
        h = self.height // Rectangle.height
        return (w * h)


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
