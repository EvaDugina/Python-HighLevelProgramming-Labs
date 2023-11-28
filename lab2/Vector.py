class MyVector:

    __x = None
    __y = None

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"<{self.x}; {self.y}>"

    def __repr__(self):
        return str(self)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __add__(self, other_vec):
        x = self.x + other_vec.x
        y = self.y + other_vec.y
        return MyVector(x, y)

    def __sub__(self, other_vec):
        x = self.x - other_vec.x
        y = self.y - other_vec.y
        return MyVector(x, y)

    def __eq__(self, other_vec):
        return self.x == other_vec.x and self.y == other_vec.y

    def __ne__(self, other_vec):
        return not self == other_vec

    def __mul__(self, other):
        if type(other) == int:
            x = self.x * other
            y = self.y * other
            return MyVector(x, y)
        elif type(other) == MyVector:
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return self * other

    def length(self):
        return (self.x**2 + self.y**2) ** 0.5