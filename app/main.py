import math

# noqa: VNE001
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(float(x), 2)
        self.y = round(float(y), 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return round(self.x * other.x + self.y * other.y, 4)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        sx, sy = start_point
        ex, ey = end_point
        return cls(ex - sx, ey - sy)

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        dot = self.x * other.x + self.y * other.y
        m1 = self.get_length()
        m2 = other.get_length()
        if m1 == 0 or m2 == 0:
            return 0
        cos_a = dot / (m1 * m2)
        cos_a = max(-1, min(1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return round(math.degrees(math.atan2(self.x, self.y)))

    def rotate(self, degrees):
        rad = math.radians(degrees)
        c = math.cos(rad)
        s = math.sin(rad)
        x = self.x * c - self.y * s
        y = self.x * s + self.y * c
        return Vector(x, y)
